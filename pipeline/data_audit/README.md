# 면접 데이터 원천 실사 도구

공개 웹에 "최신 실제 개발 직무 면접 질문 후기"가 충분한지 확인하기 위한 독립 실행 도구입니다.

## 목적

기존 크롤러를 바로 수정하기 전에 후보 URL을 모으고, 본문을 가져온 뒤 아래 등급으로 분류합니다.

- `A`: 실제 기업·부트캠프 면접 후기이며, 실제로 받은 개발 직무/CS 기술 질문이 1개 이상 있는 글
- `B`: 실제 면접 후기지만 개발 직무 기술 질문이 적거나 회사/개인 프로젝트 맥락이 강한 글
- `C`: 실제 후기는 아니지만 기술 면접 질문 은행/가이드로 보조 활용 가능한 글
- `D`: 이력서, 포트폴리오, 링크 모음, 취업 팁, 광고, 동아리/학회/스터디 면접, 노이즈

분류 결과에는 `roles`가 함께 붙습니다.

- `backend`: 백엔드, 서버, Java/Spring, DB, API 등
- `frontend`: React/Vue, JavaScript/TypeScript, 브라우저, 렌더링 등
- `devops_infra`: AWS, Docker, Kubernetes, CI/CD, 모니터링 등
- `ai_ml_data`: Python, ML/DL, 데이터 파이프라인, MLOps, RAG/LLM 등
- `cs_common`: OS, 네트워크, 자료구조, 알고리즘, Git, REST 등 공통 CS

## 실행 예시

이미 알고 있는 URL만 실사:

```bash
python -m pipeline.data_audit.audit --provider none --seed-url "https://example.com/post"
```

Naver Search API 사용:

```bash
python -m pipeline.data_audit.audit --provider naver --max-results-per-query 30 --fetch-limit 200
```

Naver는 `--max-results-per-query`가 100을 넘으면 `start` 페이지네이션으로 이어서 후보를 수집합니다.

SerpAPI 사용:

```bash
python -m pipeline.data_audit.audit --provider serpapi --max-results-per-query 10 --fetch-limit 120
```

Tistory 직접 크롤링 (API 키 불필요):

```bash
python -m pipeline.data_audit.audit --provider tistory --max-results-per-query 20 --fetch-limit 300
```

Velog GraphQL API (API 키 불필요):

```bash
python -m pipeline.data_audit.audit --provider velog --max-results-per-query 20 --fetch-limit 300
```

Google Custom Search API (`GOOGLE_API_KEY` + `GOOGLE_CSE_ID` 필요, 무료 100건/일):

```bash
python -m pipeline.data_audit.audit --provider google --max-results-per-query 10 --fetch-limit 200
```

naver + tistory + velog + google 병행 수집 (가장 많은 데이터):

```bash
python -m pipeline.data_audit.audit --provider multi --max-results-per-query 20 --fetch-limit 500
```

대량 수집을 여러 번 나눠 이어 실행:

```bash
python -m pipeline.data_audit.audit --provider multi --max-results-per-query 30 --fetch-limit 500 --resume --checkpoint-every 25
python -m pipeline.data_audit.audit --provider multi --max-results-per-query 30 --fetch-offset 500 --fetch-limit 500 --resume --checkpoint-every 25
```

Naver API 한도가 충분하면 더 크게 실행할 수 있습니다. 단, 중복과 노이즈도 같이 늘어나므로 중간 저장을 켜고 나눠 실행하는 편이 안전합니다.

```bash
python -m pipeline.data_audit.audit --provider naver --max-results-per-query 200 --fetch-limit 2000 --resume --checkpoint-every 50 --sleep-seconds 1
python -m pipeline.data_audit.audit --provider multi --max-results-per-query 100 --fetch-limit 3000 --resume --checkpoint-every 50 --sleep-seconds 1
```

결과는 기본적으로 `pipeline/data_audit/reports/`에 저장됩니다.
대량 수집 중에는 `audit_checkpoint.json`이 함께 저장되며, `--resume`을 붙이면 이미 실사한 URL은 건너뜁니다.
2023년 이후 발행 문서는 기본적으로 `freshness=recent`로 분류합니다. 기준 연도는 `--min-recent-year`로 바꿀 수 있습니다.

## 산출물

- `audit_report.json`: 전체 결과와 질문 후보를 담은 JSON
- `audit_report.md`: 사람이 검수하기 좋은 요약 리포트. 등급, 출처, 직무/기술영역 분포를 포함합니다.
- `gpt_manual_review_prompt.md`: ChatGPT에 붙여넣어 A등급 후보를 수동 재분류하기 위한 프롬프트

현재 LLM 검수는 자동 API 호출이 아니라 `gpt_manual_review_prompt.md`를 LLM에 붙여넣는 수동 검수 방식입니다.
자동 LLM 검수로 바꾸려면 규칙 기반 A/B/C 후보를 JSON으로 보내고, LLM 응답을 `result_*.json`으로 저장하는 별도 단계를 추가하면 됩니다.

## 판단 기준 제안

- 2023년 이후 `recent` A 문서가 100개 이상이면 "최신 실제 면접 후기 기반 RAG"를 메인으로 밀 수 있음
- `A` 문서가 30~100개면 실제 후기 + 질문 은행 + 채용/기술 트렌드 보강형 RAG가 현실적
- `A` 문서가 30개 미만이면 실제 후기 크롤링은 보조 기능으로 두고, 이력서 기반 질문 생성 중심으로 전환 권장

질문 단위로는 검수된 실제 질문 500~1,000개 정도부터 답변 다양성이 좋아집니다.

## Tistory가 Naver API에서 적게 잡히는 이유

Naver 검색 API의 `blog` 타겟은 **blog.naver.com 전용**이고, `webkr` 타겟은 한국 전체 웹 문서를 반환하지만 tistory 비중이 낮습니다.
Tistory는 구글 검색에 더 잘 노출되므로 `--provider tistory`, `--provider google`, `--provider multi`를 사용하면 tistory 문서를 훨씬 많이 수집할 수 있습니다.

## 현재 실사에서 드러난 주의점

- 공개 웹에는 실제 질문이 여러 개 적힌 후기가 있긴 하지만, 광고/가이드/질문은행/회고 문장이 많이 섞입니다.
- 규칙 기반 분류만으로는 A등급이 과대평가될 수 있습니다.
- 실제 KB 업로드 전에는 `gpt_manual_review_prompt.md`를 ChatGPT에 붙여넣어 "실제 기업 면접 후기인지", "개발 직무 기술 질문만 추출됐는지"를 수동 검수하는 편이 안전합니다.
- 한 번에 많이 수집할 수는 있지만 검색 API 한도, 사이트 차단, 네트워크 실패가 생길 수 있으므로 `--sleep-seconds 0.5~1.5`, `--checkpoint-every`, `--resume`을 같이 사용하는 편이 안전합니다.
