"""Audit public sources for developer interview question data.

This module answers a narrow question before changing the production crawler:
"Are there enough recent, concrete developer interview-question posts on the
public web to justify a latest-data RAG pipeline?"
Covers backend, frontend, DevOps/infra, AI/ML, and data engineering roles.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import time
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUERY_FILE = Path(__file__).with_name("queries.txt")
DEFAULT_OUTPUT_DIR = Path(__file__).with_name("reports")

USER_AGENT = (
    "Mozilla/5.0 (compatible; InterviewDataAudit/0.1; "
    "+https://example.local/interview-data-audit)"
)

INTERVIEW_TERMS = ("면접", "인터뷰", "기술 질문", "직무 질문")
TECH_TERMS = (
    # 백엔드
    "백엔드",
    "서버",
    "Java",
    "자바",
    "Spring",
    "스프링",
    "JPA",
    "DB",
    "데이터베이스",
    "REST",
    "Rest",
    "API",
    "MVC",
    "IoC",
    "DI",
    "Hibernate",
    "하이버네이트",
    "Git",
    "Branch",
    "프로토콜",
    "SQL",
    "JWT",
    "OAuth",
    "트랜잭션",
    "인덱스",
    "쿼리",
    "캐시",
    "HTTP",
    "HTTPS",
    "TCP",
    "운영체제",
    "네트워크",
    "자료구조",
    "알고리즘",
    "Node.js",
    "node.js",
    "Redis",
    "Kafka",
    "AWS",
    "Docker",
    "Kubernetes",
    "MSA",
    # 프론트엔드
    "프론트엔드",
    "React",
    "리액트",
    "Vue",
    "Angular",
    "TypeScript",
    "타입스크립트",
    "JavaScript",
    "자바스크립트",
    "HTML",
    "CSS",
    "DOM",
    "렌더링",
    "번들러",
    "Webpack",
    "Vite",
    "Next.js",
    "Nuxt",
    "상태관리",
    "Redux",
    "Recoil",
    "브라우저",
    "CORS",
    "CSR",
    "SSR",
    # DevOps / 인프라
    "DevOps",
    "인프라",
    "CI/CD",
    "파이프라인",
    "Terraform",
    "Ansible",
    "Jenkins",
    "Github Actions",
    "ArgoCD",
    "Helm",
    "모니터링",
    "Prometheus",
    "Grafana",
    "로드밸런서",
    "오토스케일링",
    "VPC",
    "서브넷",
    # AI / ML / 데이터
    "머신러닝",
    "딥러닝",
    "Python",
    "파이썬",
    "TensorFlow",
    "PyTorch",
    "모델",
    "학습",
    "데이터 파이프라인",
    "ETL",
    "Spark",
    "Hadoop",
    "MLOps",
    "특성공학",
    "피처",
    "벡터",
    "임베딩",
    "RAG",
    "LLM",
    "GPT",
    "데이터 엔지니어",
    "데이터 사이언티스트",
)
BACKEND_TERMS = TECH_TERMS  # 하위 호환 별칭
ROLE_TERMS = {
    "backend": (
        "백엔드",
        "서버",
        "Java",
        "자바",
        "Spring",
        "스프링",
        "JPA",
        "DB",
        "데이터베이스",
        "SQL",
        "JWT",
        "OAuth",
        "트랜잭션",
        "인덱스",
        "쿼리",
        "캐시",
        "HTTP",
        "HTTPS",
        "TCP",
        "Node.js",
        "Redis",
        "Kafka",
        "MSA",
    ),
    "frontend": (
        "프론트엔드",
        "React",
        "리액트",
        "Vue",
        "Angular",
        "TypeScript",
        "타입스크립트",
        "JavaScript",
        "자바스크립트",
        "HTML",
        "CSS",
        "DOM",
        "렌더링",
        "번들러",
        "Webpack",
        "Vite",
        "Next.js",
        "Nuxt",
        "상태관리",
        "Redux",
        "Recoil",
        "브라우저",
        "CORS",
        "CSR",
        "SSR",
    ),
    "devops_infra": (
        "DevOps",
        "인프라",
        "CI/CD",
        "파이프라인",
        "Terraform",
        "Ansible",
        "Jenkins",
        "Github Actions",
        "ArgoCD",
        "Helm",
        "모니터링",
        "Prometheus",
        "Grafana",
        "로드밸런서",
        "오토스케일링",
        "VPC",
        "서브넷",
        "AWS",
        "Docker",
        "Kubernetes",
    ),
    "ai_ml_data": (
        "AI",
        "머신러닝",
        "딥러닝",
        "Python",
        "파이썬",
        "TensorFlow",
        "PyTorch",
        "모델",
        "학습",
        "데이터 파이프라인",
        "ETL",
        "Spark",
        "Hadoop",
        "MLOps",
        "특성공학",
        "피처",
        "벡터",
        "임베딩",
        "RAG",
        "LLM",
        "GPT",
        "데이터 엔지니어",
        "데이터 사이언티스트",
    ),
    "cs_common": (
        "운영체제",
        "네트워크",
        "자료구조",
        "알고리즘",
        "프로토콜",
        "Git",
        "Branch",
        "API",
        "REST",
        "MVC",
    ),
}
TRUSTED_PROGRAMS = (
    "소프트웨어 마에스트로",
    "SW마에스트로",
    "소마",
    "SSAFY",
    "싸피",
    "우아한테크코스",
    "우테코",
    "부스트캠프",
    "BoostCamp",
    "카카오 테크 부트캠프",
    "카카오테크부트캠프",
    "네이버 부스트캠프",
    "42Seoul",
    "이노베이션 아카데미",
    "현대 소프티어",
    "소프티어",
    "삼성 청년 SW",
    "SWEA",
    "LG CNS",
    "DX School",
)
NOISE_TERMS = (
    "이력서 작성",
    "포트폴리오 작성",
    "링크 모음",
    "자료 모음",
    "로드맵",
    "학원 선택",
    "국비지원",
    "합격자소서",
    "채용공고",
    "입사지원서",
    "AI가 쓴",
    "ai가 쓴",
    "ChatGPT",
    "챗GPT",
    "인공지능이",
)
LOW_TRUST_DOMAINS = (
    "gall.dcinside.com",
)
GUIDE_OR_PROMOTION_DOMAINS = (
    "github.com",
    "spartaclub.kr",
    "hanghae99.spartaclub.kr",
    "f-lab.kr",
    "www.inflearn.com",
    "mentoring.inflearn.com",
    "ebook-product.kyobobook.co.kr",
    "www.yes24.com",
    "zero-base.co.kr",
)
NON_COMPANY_INTERVIEW_TERMS = (
    "동아리",
    "스터디",
    "연합동아리",
    "학회",
    "UMC",
)
WEAK_QUESTION_TERMS = (
    "마지막으로 질문",
    "질문할 내용",
    "궁금한 점",
    "순서는 잘 기억",
    "메일로 제출",
    "자기소개",
    "지원동기",
    "성격의 장단점",
    "입사 후 포부",
    "정말 나만 모르는 걸까",
    "취업/이직이 고민",
    "멘토 링크드인",
    "채용 제휴",
    "갑자기 인턴",
    "tmi",
    "서류 합격",
    "채용 사이트",
    "어떤 인재를 원하는가",
    "저는 웹 프론트엔드",
    "지원서를 작성",
    "마지막으로 하고 싶은 말",
    "회사에서 사용하고 있는",
)
ACTUAL_REVIEW_SIGNALS = (
    "받았던 질문",
    "물어봤던 질문",
    "물어보셨",
    "질문받",
    "질문 받",
    "면접에서 나온",
    "면접에서 받",
    "대답하지 못",
    "답변하지 못",
    "불합격 요인",
    "실제로",
)
QUESTION_BANK_SIGNALS = (
    "예상 질문",
    "질문 모음",
    "질문 정리",
    "문제은행",
    "면접 대비",
    "모범 답변",
)
QUESTION_HINTS = (
    "무엇",
    "뭔지",
    "차이",
    "설명",
    "어떻게",
    "왜",
    "경험",
    "장단점",
    "원리",
    "동작",
    "해결",
)


@dataclass
class Candidate:
    query: str
    title: str
    url: str
    source: str


@dataclass
class AuditResult:
    url: str
    title: str
    source: str
    query: str
    grade: str
    score: int
    reason: str
    published_at: str | None
    content_chars: int
    question_count: int
    question_samples: list[str]
    roles: list[str] = field(default_factory=list)
    freshness: str = "unknown"


def load_queries(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def load_seed_urls(path: Path | None, inline_urls: list[str]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for url in inline_urls:
        candidates.append(Candidate(query="seed", title="", url=url, source=guess_source(url)))

    if path and path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            url = line.strip()
            if url and not url.startswith("#"):
                candidates.append(Candidate(query="seed_file", title="", url=url, source=guess_source(url)))

    return candidates


def guess_source(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if "tistory" in host:
        return "tistory"
    if "velog" in host:
        return "velog"
    if "jobkorea" in host:
        return "jobkorea"
    if "saramin" in host:
        return "saramin"
    if "naver" in host:
        return "naver"
    return host or "unknown"


def search_naver(queries: list[str], max_results_per_query: int) -> list[Candidate]:
    client_id = os.getenv("NAVER_CLIENT_ID", "")
    client_secret = os.getenv("NAVER_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        print("[audit] NAVER_CLIENT_ID / NAVER_CLIENT_SECRET가 없어 Naver 검색을 건너뜁니다.")
        return []

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "User-Agent": USER_AGENT,
    }
    results: list[Candidate] = []
    targets = [item.strip() for item in os.getenv("NAVER_SEARCH_TARGETS", "blog,webkr").split(",")]

    for query in queries:
        for target in targets:
            url = f"https://openapi.naver.com/v1/search/{target}.json"
            fetched = 0
            start = 1
            while fetched < max_results_per_query and start <= 1000:
                display = min(100, max_results_per_query - fetched)
                params = {
                    "query": query,
                    "display": display,
                    "start": start,
                    "sort": "date",
                }
                try:
                    resp = requests.get(url, params=params, headers=headers, timeout=10)
                    resp.raise_for_status()
                    items = resp.json().get("items", [])
                except Exception as exc:
                    print(f"[audit] Naver 검색 실패 query={query!r}, target={target}, start={start}: {exc}")
                    break

                if not items:
                    break

                for item in items:
                    link = item.get("link") or item.get("originallink")
                    if not link:
                        continue
                    results.append(
                        Candidate(
                            query=query,
                            title=clean_text(item.get("title", "")),
                            url=link,
                            source=guess_source(link),
                        )
                    )
                    fetched += 1
                    if fetched >= max_results_per_query:
                        break

                start += len(items)
                time.sleep(0.2)
    return dedupe_candidates(results)


def search_serpapi(queries: list[str], max_results_per_query: int) -> list[Candidate]:
    api_key = os.getenv("SERPAPI_API_KEY", "")
    if not api_key:
        print("[audit] SERPAPI_API_KEY가 없어 SerpAPI 검색을 건너뜁니다.")
        return []

    results: list[Candidate] = []
    for query in queries:
        params = {
            "engine": "google",
            "q": query,
            "num": max_results_per_query,
            "hl": "ko",
            "gl": "kr",
            "api_key": api_key,
        }
        try:
            resp = requests.get("https://serpapi.com/search.json", params=params, timeout=20)
            resp.raise_for_status()
            items = resp.json().get("organic_results", [])
        except Exception as exc:
            print(f"[audit] SerpAPI 검색 실패 query={query!r}: {exc}")
            continue

        for item in items:
            link = item.get("link")
            if not link:
                continue
            results.append(
                Candidate(
                    query=query,
                    title=clean_text(item.get("title", "")),
                    url=link,
                    source=guess_source(link),
                )
            )
        time.sleep(0.2)
    return dedupe_candidates(results)


def search_tistory(queries: list[str], max_results_per_query: int) -> list[Candidate]:
    """Tistory 검색 페이지를 직접 크롤링해 후보 URL을 수집합니다.

    Naver API는 blog.naver.com 위주로 반환하기 때문에 tistory 글이 거의 잡히지 않습니다.
    Tistory 검색(https://www.tistory.com/search)은 로그인 없이 HTML을 제공하므로
    직접 파싱해 후보를 수집합니다.
    """
    results: list[Candidate] = []
    for query in queries:
        url = "https://www.tistory.com/search"
        params = {"q": query}
        try:
            resp = requests.get(
                url,
                params=params,
                headers={"User-Agent": USER_AGENT},
                timeout=15,
            )
            resp.raise_for_status()
        except Exception as exc:
            print(f"[audit] Tistory 검색 실패 query={query!r}: {exc}")
            time.sleep(0.5)
            continue

        links = re.findall(
            r'href=["\']((https?://[^.]+\.tistory\.com/[^"\' >]+))["\']',
            resp.text,
        )
        seen_in_query: set[str] = set()
        for link in links:
            post_url = link[0].split("?")[0].rstrip("/")
            if post_url in seen_in_query:
                continue
            seen_in_query.add(post_url)
            results.append(
                Candidate(
                    query=query,
                    title="",
                    url=post_url,
                    source="tistory",
                )
            )
            if len(seen_in_query) >= max_results_per_query:
                break
        time.sleep(0.5)
    return dedupe_candidates(results)


def search_velog(queries: list[str], max_results_per_query: int) -> list[Candidate]:
    """Velog GraphQL API로 후보 URL을 수집합니다.

    Velog는 공개 GraphQL 엔드포인트(https://v3.velog.io/graphql)를 제공합니다.
    """
    results: list[Candidate] = []
    gql_query = """
    query SearchPosts($keyword: String!, $offset: Int) {
      searchPosts(keyword: $keyword, offset: $offset) {
        posts {
          id
          title
          url_slug
          user { username }
        }
      }
    }
    """
    for query in queries:
        offset = 0
        fetched = 0
        while fetched < max_results_per_query:
            try:
                resp = requests.post(
                    "https://v3.velog.io/graphql",
                    json={"query": gql_query, "variables": {"keyword": query, "offset": offset}},
                    headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
                    timeout=15,
                )
                resp.raise_for_status()
                posts = (
                    resp.json()
                    .get("data", {})
                    .get("searchPosts", {})
                    .get("posts", [])
                )
            except Exception as exc:
                print(f"[audit] Velog 검색 실패 query={query!r}: {exc}")
                break
            if not posts:
                break
            for post in posts:
                username = post.get("user", {}).get("username", "")
                slug = post.get("url_slug", "")
                if username and slug:
                    post_url = f"https://velog.io/@{username}/{slug}"
                    results.append(
                        Candidate(
                            query=query,
                            title=clean_text(post.get("title", "")),
                            url=post_url,
                            source="velog",
                        )
                    )
                    fetched += 1
                    if fetched >= max_results_per_query:
                        break
            offset += len(posts)
            time.sleep(0.3)
    return dedupe_candidates(results)


def search_google(queries: list[str], max_results_per_query: int) -> list[Candidate]:
    """Google Custom Search JSON API로 후보 URL을 수집합니다.

    무료 티어: 100건/일. GOOGLE_API_KEY와 GOOGLE_CSE_ID가 필요합니다.
    Google Cloud Console에서 Custom Search API를 활성화하고,
    https://programmablesearchengine.google.com 에서 검색 엔진 ID(CSE ID)를 발급받으세요.
    """
    api_key = os.getenv("GOOGLE_API_KEY", "")
    cse_id = os.getenv("GOOGLE_CSE_ID", "")
    if not api_key or not cse_id:
        print("[audit] GOOGLE_API_KEY / GOOGLE_CSE_ID가 없어 Google 검색을 건너뜁니다.")
        return []

    results: list[Candidate] = []
    for query in queries:
        start = 1
        fetched = 0
        while fetched < max_results_per_query:
            batch = min(10, max_results_per_query - fetched)
            params = {
                "key": api_key,
                "cx": cse_id,
                "q": query,
                "num": batch,
                "start": start,
                "lr": "lang_ko",
                "gl": "kr",
            }
            try:
                resp = requests.get(
                    "https://www.googleapis.com/customsearch/v1",
                    params=params,
                    timeout=15,
                )
                resp.raise_for_status()
                items = resp.json().get("items", [])
            except Exception as exc:
                print(f"[audit] Google 검색 실패 query={query!r}: {exc}")
                break
            if not items:
                break
            for item in items:
                link = item.get("link")
                if not link:
                    continue
                results.append(
                    Candidate(
                        query=query,
                        title=clean_text(item.get("title", "")),
                        url=link,
                        source=guess_source(link),
                    )
                )
                fetched += 1
            start += batch
            time.sleep(0.3)
    return dedupe_candidates(results)


def dedupe_candidates(candidates: Iterable[Candidate]) -> list[Candidate]:
    seen: set[str] = set()
    unique: list[Candidate] = []
    for candidate in candidates:
        normalized_url = normalize_url(candidate.url)
        if normalized_url in seen:
            continue
        seen.add(normalized_url)
        unique.append(candidate)
    return unique


def normalize_url(url: str) -> str:
    return url.split("#", 1)[0].rstrip("/")


def fetch_html(url: str) -> str | None:
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)
        resp.raise_for_status()
        if "text/html" not in resp.headers.get("Content-Type", ""):
            return None
        try:
            return resp.content.decode("utf-8")
        except UnicodeDecodeError:
            encoding = resp.apparent_encoding or resp.encoding or "utf-8"
            return resp.content.decode(encoding, errors="replace")
    except Exception as exc:
        print(f"[audit] 본문 수집 실패 url={url}: {exc}")
        return None


def extract_title(raw_html: str, fallback: str) -> str:
    for pattern in (
        r'<meta\s+property=["\']og:title["\']\s+content=["\']([^"\']+)["\']',
        r'<meta\s+name=["\']title["\']\s+content=["\']([^"\']+)["\']',
        r"<title[^>]*>(.*?)</title>",
        r"<h1[^>]*>(.*?)</h1>",
    ):
        match = re.search(pattern, raw_html, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return clean_text(match.group(1))
    return fallback


def extract_published_at(raw_html: str, text: str) -> str | None:
    meta_patterns = (
        r'<meta\s+property=["\']article:published_time["\']\s+content=["\']([^"\']+)["\']',
        r'<time[^>]+datetime=["\']([^"\']+)["\']',
    )
    for pattern in meta_patterns:
        match = re.search(pattern, raw_html, flags=re.IGNORECASE)
        if match:
            return clean_text(match.group(1))

    date_patterns = (
        r"(20\d{2})[.\-/년]\s*(\d{1,2})[.\-/월]\s*(\d{1,2})",
        r"(20\d{2})\s*년\s*(\d{1,2})\s*월",
    )
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            parts = [int(part) for part in match.groups()]
            if len(parts) == 2:
                parts.append(1)
            try:
                return datetime(parts[0], parts[1], parts[2]).date().isoformat()
            except ValueError:
                continue
    return None


def classify_freshness(published_at: str | None, min_recent_year: int) -> str:
    if not published_at or not published_at[:4].isdigit():
        return "unknown"
    return "recent" if int(published_at[:4]) >= min_recent_year else "old"


def html_to_text(raw_html: str) -> str:
    without_scripts = re.sub(r"<(script|style).*?</\1>", " ", raw_html, flags=re.IGNORECASE | re.DOTALL)
    with_breaks = re.sub(r"</(p|div|li|h[1-6]|br|tr)>", "\n", without_scripts, flags=re.IGNORECASE)
    without_tags = re.sub(r"<[^>]+>", " ", with_breaks)
    value = html.unescape(without_tags)
    value = re.sub(r"[ \t\f\v]+", " ", value)
    value = re.sub(r" *\n *", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def clean_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_candidate_lines(text: str) -> list[str]:
    lines = []
    for raw_line in re.split(r"[\n\r]+|(?<=[.?!])\s+", text):
        line = raw_line.strip(" \t-•*0123456789.)(")
        if 8 <= len(line) <= 180:
            lines.append(line)
    return lines


def extract_question_samples(text: str) -> list[str]:
    samples: list[str] = []
    for line in split_candidate_lines(text):
        if any(term.lower() in line.lower() for term in WEAK_QUESTION_TERMS):
            continue
        has_question_mark = "?" in line or "？" in line
        has_question_hint = any(term in line for term in QUESTION_HINTS)
        has_tech_hint = any(term.lower() in line.lower() for term in TECH_TERMS)
        if has_tech_hint and (has_question_mark or has_question_hint):
            if not any(noise in line for noise in NOISE_TERMS):
                samples.append(line)
        if len(samples) >= 10:
            break
    return samples


def count_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def detect_roles(text: str, question_samples: list[str]) -> list[str]:
    target = f"{text}\n" + "\n".join(question_samples)
    role_scores = {
        role: count_terms(target, terms)
        for role, terms in ROLE_TERMS.items()
    }
    roles = [
        role
        for role, score in sorted(role_scores.items(), key=lambda item: (-item[1], item[0]))
        if score > 0
    ]
    return roles or ["unknown"]


def classify(candidate: Candidate, title: str, text: str, min_content_chars: int) -> AuditResult:
    joined = f"{title}\n{text}"
    question_samples = extract_question_samples(text)
    question_count = len(question_samples)
    roles = detect_roles(joined, question_samples)

    actual_hits = sum(1 for term in ACTUAL_REVIEW_SIGNALS if term in joined)
    question_bank_hits = sum(1 for term in QUESTION_BANK_SIGNALS if term in joined)
    tech_hits = count_terms(joined, TECH_TERMS)
    interview_hits = sum(1 for term in INTERVIEW_TERMS if term in joined)
    noise_hits = sum(1 for term in NOISE_TERMS if term in joined)
    low_trust_source = candidate.source in LOW_TRUST_DOMAINS
    guide_or_promotion_source = candidate.source in GUIDE_OR_PROMOTION_DOMAINS
    non_company_hits = sum(1 for term in NON_COMPANY_INTERVIEW_TERMS if term.lower() in joined.lower())
    trusted_program_hit = any(term.lower() in joined.lower() for term in TRUSTED_PROGRAMS)
    review_title_signal = "면접" in title and "후기" in title

    score = question_count * 3 + actual_hits * 8 + tech_hits * 2 + interview_hits * 2
    score -= question_bank_hits * 3 + noise_hits * 10
    score -= non_company_hits * 6
    if low_trust_source:
        score -= 20
    if guide_or_promotion_source:
        score -= 18
    if len(text) < min_content_chars:
        score -= 12

    if low_trust_source:
        grade = "D"
        reason = "신뢰도가 낮은 커뮤니티 출처라 KB 원천 데이터에서 제외 권장"
    elif guide_or_promotion_source:
        if question_count >= 5 and tech_hits > 0:
            grade = "C"
            reason = "실제 후기보다 가이드/질문은행/홍보성 출처라 보조 자료로만 활용 권장"
        else:
            grade = "D"
            reason = "가이드/홍보성 출처이며 기술 질문 후보가 부족함"
    elif non_company_hits >= 2 and question_count < 5 and not trusted_program_hit:
        grade = "D"
        reason = "기업/부트캠프 면접보다 동아리/스터디/학회 면접 성격이 강함"
    elif noise_hits >= 2 or (noise_hits >= 1 and question_count == 0):
        grade = "D"
        reason = "노이즈 키워드가 강하고 실제 질문 후보가 부족함"
    elif len(text) < min_content_chars and question_count < 3:
        grade = "D"
        reason = f"본문이 {min_content_chars}자 미만이고 질문 후보가 부족함"
    elif (actual_hits > 0 or review_title_signal or trusted_program_hit) and question_count >= 1 and tech_hits > 0:
        grade = "A"
        reason = "실제 면접 신호와 구체 기술 질문 후보가 있음"
    elif (actual_hits > 0 or review_title_signal or trusted_program_hit) and question_count >= 1:
        grade = "B"
        reason = "실제 면접 후기 신호는 있으나 기술 질문 밀도가 낮음"
    elif question_bank_hits > 0 and question_count >= 5:
        grade = "C"
        reason = "예상 질문/질문 은행 성격으로 활용 가능"
    elif question_count >= 5 and tech_hits > 0 and interview_hits > 0:
        grade = "C"
        reason = "개발 직무 기술면접 질문 후보는 많지만 실제 후기 신호가 약함"
    else:
        grade = "D"
        reason = "실제 면접 질문 데이터로 쓰기 어려움"

    return AuditResult(
        url=candidate.url,
        title=title or candidate.title,
        source=candidate.source,
        query=candidate.query,
        grade=grade,
        score=score,
        reason=reason,
        published_at=None,
        content_chars=len(text),
        question_count=question_count,
        question_samples=question_samples[:5],
        roles=roles,
    )


def audit_candidates(
    candidates: list[Candidate],
    fetch_limit: int,
    min_content_chars: int,
    sleep_seconds: float,
    min_recent_year: int,
    existing_results: list[AuditResult] | None = None,
    checkpoint_path: Path | None = None,
    checkpoint_every: int = 25,
) -> list[AuditResult]:
    results: list[AuditResult] = list(existing_results or [])
    seen_urls = {normalize_url(result.url) for result in results}
    target_candidates = candidates[:fetch_limit]
    total = len(target_candidates)
    processed_since_checkpoint = 0

    for index, candidate in enumerate(target_candidates, 1):
        if normalize_url(candidate.url) in seen_urls:
            print(f"[audit] ({index}/{total}) skip existing {candidate.url}")
            continue

        print(f"[audit] ({index}/{total}) {candidate.url}")
        raw_html = fetch_html(candidate.url)
        if not raw_html:
            continue

        text = html_to_text(raw_html)
        title = extract_title(raw_html, candidate.title)
        result = classify(candidate, title, text, min_content_chars)
        result.published_at = extract_published_at(raw_html, text)
        result.freshness = classify_freshness(result.published_at, min_recent_year)
        results.append(result)
        seen_urls.add(normalize_url(candidate.url))
        processed_since_checkpoint += 1

        if checkpoint_path and checkpoint_every > 0 and processed_since_checkpoint >= checkpoint_every:
            write_checkpoint(results, checkpoint_path)
            processed_since_checkpoint = 0

        time.sleep(sleep_seconds)

    if checkpoint_path:
        write_checkpoint(results, checkpoint_path)

    return sorted(results, key=lambda item: (item.grade, -item.score, item.source))


def load_results(path: Path) -> list[AuditResult]:
    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))
    raw_results = data.get("results", [])
    results: list[AuditResult] = []
    for item in raw_results:
        item.setdefault("roles", ["unknown"])
        item.setdefault("freshness", classify_freshness(item.get("published_at"), 2023))
        try:
            results.append(AuditResult(**item))
        except TypeError:
            continue
    return results


def write_checkpoint(results: list[AuditResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "summary": summarize(results),
        "results": [asdict(result) for result in results],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[audit] checkpoint saved: {path}")


def summarize(results: list[AuditResult]) -> dict:
    grade_counts = Counter(result.grade for result in results)
    source_counts = Counter(result.source for result in results)
    role_counts = Counter(role for result in results for role in (result.roles or ["unknown"]))
    freshness_counts = Counter(result.freshness or "unknown" for result in results)
    recent_grade_counts = Counter(result.grade for result in results if result.freshness == "recent")
    recent_grade_a = [
        result
        for result in results
        if result.grade == "A" and result.published_at and result.published_at[:4].isdigit()
    ]
    recent_grade_a.sort(key=lambda item: item.published_at or "", reverse=True)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_fetched": len(results),
        "grade_counts": dict(sorted(grade_counts.items())),
        "source_counts": dict(source_counts.most_common()),
        "role_counts": dict(role_counts.most_common()),
        "freshness_counts": dict(freshness_counts.most_common()),
        "recent_grade_counts": dict(sorted(recent_grade_counts.items())),
        "latest_grade_a_date": recent_grade_a[0].published_at if recent_grade_a else None,
        "avg_questions_per_grade_a_doc": round(
            sum(result.question_count for result in results if result.grade == "A")
            / max(1, grade_counts.get("A", 0)),
            2,
        ),
    }


def write_reports(results: list[AuditResult], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary = summarize(results)
    payload = {
        "summary": summary,
        "results": [asdict(result) for result in results],
    }
    (output_dir / "audit_report.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / "audit_report.md").write_text(render_markdown(summary, results), encoding="utf-8")
    (output_dir / "gpt_manual_review_prompt.md").write_text(
        render_manual_review_prompt(results),
        encoding="utf-8",
    )


def render_markdown(summary: dict, results: list[AuditResult]) -> str:
    lines = [
        "# 면접 데이터 원천 실사 리포트",
        "",
        f"- 생성 시각(UTC): `{summary['generated_at']}`",
        f"- 수집 성공 문서 수: `{summary['total_fetched']}`",
        f"- 등급별 개수: `{summary['grade_counts']}`",
        f"- 소스별 개수: `{summary['source_counts']}`",
        f"- 직무/기술영역별 개수: `{summary['role_counts']}`",
        f"- 최신성 개수: `{summary['freshness_counts']}`",
        f"- 최신 문서 등급별 개수: `{summary['recent_grade_counts']}`",
        f"- A등급 평균 질문 후보 수: `{summary['avg_questions_per_grade_a_doc']}`",
        f"- 최신 A등급 문서 날짜: `{summary['latest_grade_a_date']}`",
        "",
        "## A등급 후보",
        "",
    ]

    grade_a = [result for result in results if result.grade == "A"]
    if not grade_a:
        lines.append("A등급 후보가 없습니다.")
    else:
        for result in grade_a[:30]:
            lines.extend(
                [
                    f"### {result.title}",
                    "",
                    f"- URL: {result.url}",
                    f"- Source: `{result.source}`",
                    f"- Roles: `{result.roles}`",
                    f"- Published: `{result.published_at}`",
                    f"- Freshness: `{result.freshness}`",
                    f"- Score: `{result.score}`",
                    f"- Questions: `{result.question_count}`",
                    f"- Reason: {result.reason}",
                    "",
                ]
            )
            for sample in result.question_samples:
                lines.append(f"  - {sample}")
            lines.append("")

    lines.extend(["## 전체 결과", ""])
    for result in results:
        lines.append(
            f"- `{result.grade}` score={result.score} q={result.question_count} "
            f"freshness={result.freshness} roles={','.join(result.roles or ['unknown'])} "
            f"source={result.source} title={result.title} url={result.url}"
        )
    lines.append("")
    return "\n".join(lines)


def render_manual_review_prompt(results: list[AuditResult]) -> str:
    candidates = [result for result in results if result.grade == "A"]
    lines = [
        "# ChatGPT 수동 검수 프롬프트",
        "",
        "아래 후보들은 규칙 기반 크롤링 실사에서 A등급으로 분류된 문서입니다.",
        "AI 모의면접 RAG Knowledge Base에 넣을 수 있는지 A/B/C/D로 재분류해주세요.",
        "",
        "등급 기준:",
        "- A: 실제 기업 면접 후기이며, 실제로 받은 개발 직무/CS 기술 질문이 3개 이상 있음",
        "- B: 실제 기업 면접 후기지만 질문이 적거나, 회사/개인 프로젝트 맥락이 강해 일반화가 어려움",
        "- C: 실제 후기는 아니지만 개발 직무 기술면접 질문 은행/가이드로 보조 활용 가능",
        "- D: 광고, 강의/멘토링 홍보, 동아리/부트캠프 면접, 개인 회고/답변문, 비기술 질문, 노이즈",
        "",
        "주의:",
        "- 자기소개, 지원동기, 마지막 질문, 회사 위치/조직 관련 질문은 개발 직무 기술 질문으로 세지 마세요.",
        "- 답변/회고 문장은 질문으로 세지 마세요.",
        "- 특정 회사 내부 시스템에 지나치게 묶인 질문은 B로 낮춰주세요.",
        "- GitHub 질문은행, 강의 페이지, 멘토링 홍보, 취업 가이드는 A가 될 수 없습니다.",
        "",
        "아래 JSON 형식으로만 답해주세요:",
        "",
        "```json",
        "{",
        '  "summary": {',
        '    "usable_a_count": 0,',
        '    "recommendation": "실제 후기 기반 RAG를 메인으로 써도 되는지에 대한 짧은 판단"',
        "  },",
        '  "items": [',
        '    {',
        '      "index": 1,',
        '      "grade": "A|B|C|D",',
        '      "reason": "짧은 이유",',
        '      "roles": ["backend|frontend|devops_infra|ai_ml_data|cs_common|unknown"],',
        '      "usable_questions": ["실제로 쓸 수 있는 개발 직무/CS 기술 질문만"]',
        "    }",
        "  ]",
        "}",
        "```",
        "",
        "검수 대상:",
        "",
    ]

    for index, result in enumerate(candidates, 1):
        lines.extend(
            [
                f"## {index}. {result.title}",
                "",
                f"- URL: {result.url}",
                f"- Source: {result.source}",
                f"- Roles: {result.roles}",
                f"- Published: {result.published_at}",
                f"- Freshness: {result.freshness}",
                f"- Rule score: {result.score}",
                f"- Rule reason: {result.reason}",
                "- Rule question samples:",
            ]
        )
        for sample in result.question_samples:
            lines.append(f"  - {sample}")
        lines.append("")

    return "\n".join(lines)


def collect_candidates(provider: str, queries: list[str], max_results_per_query: int) -> list[Candidate]:
    if provider == "naver":
        return search_naver(queries, max_results_per_query)
    if provider == "serpapi":
        return search_serpapi(queries, max_results_per_query)
    if provider == "tistory":
        return search_tistory(queries, max_results_per_query)
    if provider == "velog":
        return search_velog(queries, max_results_per_query)
    if provider == "google":
        return search_google(queries, max_results_per_query)
    if provider == "multi":
        all_candidates: list[Candidate] = []
        all_candidates.extend(search_naver(queries, max_results_per_query))
        all_candidates.extend(search_tistory(queries, max_results_per_query))
        all_candidates.extend(search_velog(queries, max_results_per_query))
        all_candidates.extend(search_google(queries, max_results_per_query))
        return dedupe_candidates(all_candidates)
    if provider == "auto":
        candidates = search_naver(queries, max_results_per_query)
        if candidates:
            return candidates
        return search_serpapi(queries, max_results_per_query)
    return []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit public developer interview-question sources.")
    parser.add_argument(
        "--provider",
        choices=["auto", "naver", "serpapi", "tistory", "velog", "google", "multi", "none"],
        default="auto",
        help=(
            "auto: naver 우선, 없으면 serpapi | naver: 네이버 검색 API | serpapi: SerpAPI(구글) | "
            "tistory: tistory 직접 크롤링 | velog: velog GraphQL API | "
            "google: Google Custom Search API | multi: naver+tistory+velog+google 병행 | none: seed URL만 사용"
        ),
    )
    parser.add_argument("--query-file", type=Path, default=DEFAULT_QUERY_FILE)
    parser.add_argument("--seed-file", type=Path, default=None)
    parser.add_argument("--seed-url", action="append", default=[])
    parser.add_argument("--max-results-per-query", type=int, default=10)
    parser.add_argument("--fetch-limit", type=int, default=120)
    parser.add_argument(
        "--min-recent-year",
        type=int,
        default=2023,
        help="이 연도 이후 발행 문서를 최신(recent)으로 분류합니다. 기본값은 2023입니다.",
    )
    parser.add_argument(
        "--fetch-offset",
        type=int,
        default=0,
        help="후보 URL 목록에서 앞쪽 N개를 건너뛰고 실사합니다. 큰 작업을 여러 배치로 나눌 때 사용합니다.",
    )
    parser.add_argument("--min-content-chars", type=int, default=800)
    parser.add_argument("--sleep-seconds", type=float, default=0.5)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="output-dir의 audit_checkpoint.json 또는 audit_report.json을 읽어 이미 실사한 URL을 건너뜁니다.",
    )
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=25,
        help="N개 문서 실사마다 audit_checkpoint.json을 저장합니다. 0이면 중간 저장을 끕니다.",
    )
    return parser.parse_args()


def main() -> None:
    load_dotenv(ROOT / ".env")
    args = parse_args()

    queries = load_queries(args.query_file)
    candidates = load_seed_urls(args.seed_file, args.seed_url)
    candidates.extend(collect_candidates(args.provider, queries, args.max_results_per_query))
    candidates = dedupe_candidates(candidates)

    print(f"[audit] 후보 URL {len(candidates)}개")
    if not candidates:
        print("[audit] 후보 URL이 없습니다. 검색 API 키를 설정하거나 --seed-url / --seed-file을 사용하세요.")
        return

    if args.fetch_offset > 0:
        candidates = candidates[args.fetch_offset :]
        print(f"[audit] fetch offset 적용: 앞쪽 {args.fetch_offset}개 건너뜀, 남은 후보 {len(candidates)}개")

    checkpoint_path = args.output_dir / "audit_checkpoint.json"
    existing_results: list[AuditResult] = []
    if args.resume:
        existing_results = load_results(checkpoint_path)
        if not existing_results:
            existing_results = load_results(args.output_dir / "audit_report.json")
        for result in existing_results:
            result.freshness = classify_freshness(result.published_at, args.min_recent_year)
        print(f"[audit] resume: 기존 결과 {len(existing_results)}개 로드")

    results = audit_candidates(
        candidates=candidates,
        fetch_limit=args.fetch_limit,
        min_content_chars=args.min_content_chars,
        sleep_seconds=args.sleep_seconds,
        min_recent_year=args.min_recent_year,
        existing_results=existing_results,
        checkpoint_path=checkpoint_path,
        checkpoint_every=args.checkpoint_every,
    )
    write_reports(results, args.output_dir)
    print(f"[audit] 리포트 저장 완료: {args.output_dir}")
    print(json.dumps(summarize(results), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
