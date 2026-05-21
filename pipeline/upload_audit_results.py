"""
수동 검수 A등급 문서를 S3에 업로드하고 Knowledge Base Sync를 트리거한다.

사용법:
    python -m pipeline.upload_audit_results                  # result_500.json 기본
    python -m pipeline.upload_audit_results --input pipeline/data_audit/result_500.json
    python -m pipeline.upload_audit_results --source-report pipeline/data_audit/reports/audit_report.json
    python -m pipeline.upload_audit_results --dry-run        # 실제 업로드 없이 내용만 출력
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "interview-crawled-data")
S3_PREFIX = os.getenv("S3_PREFIX", "crawled/")
KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID", "")

DEFAULT_INPUT = Path(__file__).resolve().parents[0] / "data_audit" / "result_500.json"
DEFAULT_SOURCE_REPORT = (
    Path(__file__).resolve().parents[0]
    / "data_audit"
    / "reports"
    / "audit_report.json"
)


def load_items(input_path: Path, source_report_path: Path | None) -> list[dict]:
    """수동 검수 결과와 원본 audit report 메타데이터를 합친다."""
    data = json.loads(input_path.read_text(encoding="utf-8"))
    items = data.get("items") or data.get("results") or []

    source_results: list[dict] = []
    if source_report_path and source_report_path.exists():
        source_data = json.loads(source_report_path.read_text(encoding="utf-8"))
        source_results = source_data.get("results") or source_data.get("items") or []

    if not source_results:
        return items

    merged: list[dict] = []
    for item in items:
        source = {}
        index = item.get("index")
        if isinstance(index, int) and 1 <= index <= len(source_results):
            source = source_results[index - 1]

        combined = {**source, **item}
        if source:
            combined["audit_grade"] = source.get("grade", "")
            combined["manual_grade"] = item.get("grade", "")
            combined["audit_reason"] = source.get("reason", "")
            combined["manual_reason"] = item.get("reason", "")
        merged.append(combined)

    return merged


def build_document_text(item: dict) -> str:
    """A등급 항목 1건을 KB에 넣을 텍스트 포맷으로 변환한다."""
    title = item.get("title", "")
    url = item.get("url", "")
    source = item.get("source", "")
    published = item.get("published_at", "") or ""
    reason = item.get("manual_reason") or item.get("reason", "")
    audit_reason = item.get("audit_reason", "")
    questions: list[str] = item.get("usable_questions", [])

    lines = [
        "[메타데이터]",
        f"제목: {title or '미상'}",
        f"출처: {url or '미상'}",
        f"소스: {source or '미상'}",
        f"발행일: {published[:10] if published else '미상'}",
        f"수집일: {datetime.now(timezone.utc).date().isoformat()}",
        f"수동 검수 근거: {reason or '미상'}",
    ]
    if audit_reason:
        lines.append(f"규칙 기반 분류 근거: {audit_reason}")

    lines.extend(["", "[실제 면접 질문 목록]"])
    if questions:
        for q in questions:
            lines.append(f"- {q}")
    else:
        lines.append("(질문 샘플 없음)")

    return "\n".join(lines)


def print_safe(value: str) -> None:
    """Windows 콘솔 인코딩이 일부 문자를 못 찍어도 dry-run이 중단되지 않게 한다."""
    encoding = sys.stdout.encoding or "utf-8"
    safe_value = value.encode(encoding, errors="replace").decode(encoding)
    print(safe_value)


def build_s3_key(item: dict) -> str:
    index = item.get("index")
    if isinstance(index, int):
        return f"{S3_PREFIX}audit/a-{index:04d}.txt"
    payload = json.dumps(item, ensure_ascii=False, sort_keys=True)
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:12]
    return f"{S3_PREFIX}audit/a-unknown-{digest}.txt"


def upload_to_s3(item: dict, text: str, s3_client, dry_run: bool) -> str:
    s3_key = build_s3_key(item)

    if dry_run:
        print(f"[DRY-RUN] 업로드 예정: s3://{S3_BUCKET_NAME}/{s3_key}")
        print_safe(f"{text[:300]} ...\n")
        return s3_key

    s3_client.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=s3_key,
        Body=text.encode("utf-8"),
        ContentType="text/plain; charset=utf-8",
    )
    print(f"[S3] 업로드 완료: s3://{S3_BUCKET_NAME}/{s3_key}")
    return s3_key


def get_data_source_id(kb_id: str) -> str:
    """KB의 첫 번째 데이터 소스 ID를 자동으로 조회한다."""
    client = boto3.client("bedrock-agent", region_name=AWS_REGION)
    resp = client.list_data_sources(knowledgeBaseId=kb_id)
    sources = resp.get("dataSourceSummaries", [])
    if not sources:
        raise RuntimeError(f"KB {kb_id}에 데이터 소스가 없습니다.")
    ds_id = sources[0]["dataSourceId"]
    print(f"[KB] 데이터 소스 ID 자동 조회: {ds_id}")
    return ds_id


def sync_kb(kb_id: str, dry_run: bool):
    if dry_run:
        print(f"[DRY-RUN] KB Sync 생략 (kb_id={kb_id})")
        return
    if not kb_id:
        print("[KB] KNOWLEDGE_BASE_ID 미설정 → Sync 생략")
        return

    ds_id = get_data_source_id(kb_id)
    client = boto3.client("bedrock-agent", region_name=AWS_REGION)
    resp = client.start_ingestion_job(knowledgeBaseId=kb_id, dataSourceId=ds_id)
    job_id = resp["ingestionJob"]["ingestionJobId"]
    print(f"[KB] 동기화 시작 → jobId={job_id}")
    print("[KB] AWS 콘솔 Knowledge Bases → Sync 탭에서 진행 상황 확인 가능")


def main():
    parser = argparse.ArgumentParser(description="A등급 면접 후기를 S3/KB에 업로드")
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="result JSON 파일 경로 (기본: pipeline/data_audit/result_500.json)",
    )
    parser.add_argument(
        "--grade",
        default="A",
        help="업로드할 등급 (기본: A)",
    )
    parser.add_argument(
        "--source-report",
        type=Path,
        default=DEFAULT_SOURCE_REPORT,
        help=(
            "원본 audit_report.json 경로. result_500.json 같은 수동 검수 결과의 "
            "index를 원본 메타데이터와 merge할 때 사용"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="실제 업로드 없이 내용만 출력",
    )
    parser.add_argument(
        "--no-sync",
        action="store_true",
        help="S3 업로드 후 KB Sync 트리거 생략",
    )
    args = parser.parse_args()

    items = load_items(args.input, args.source_report)

    targets = [it for it in items if it.get("grade") == args.grade]
    print(f"[업로드] {args.grade}등급 {len(targets)}건 처리 시작")

    if not targets:
        print("업로드할 항목 없음.")
        return

    s3 = boto3.client("s3", region_name=AWS_REGION) if not args.dry_run else None
    uploaded = 0

    for item in targets:
        text = build_document_text(item)
        upload_to_s3(item, text, s3, dry_run=args.dry_run)
        uploaded += 1

    print(f"\n[완료] 총 {uploaded}건 {'(dry-run)' if args.dry_run else '업로드 완료'}")

    if not args.no_sync:
        sync_kb(KNOWLEDGE_BASE_ID, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
