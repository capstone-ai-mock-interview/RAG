# 면접 데이터 원천 실사 도구

공개 웹에 "최신 실제 백엔드 면접 질문 후기"가 충분한지 확인하기 위한 독립 실행 도구입니다.

## 목적

기존 크롤러를 바로 수정하기 전에 후보 URL을 모으고, 본문을 가져온 뒤 아래 등급으로 분류합니다.

- `A`: 실제 기업·부트캠프 면접 후기이며, 실제로 받은 백엔드/CS 기술 질문이 1개 이상 있는 글
- `B`: 실제 면접 후기지만 백엔드 기술 질문이 없거나 회사/개인 프로젝트 맥락이 강한 글
- `C`: 실제 후기는 아니지만 기술 면접 질문 은행/가이드로 보조 활용 가능한 글
- `D`: 이력서, 포트폴리오, 링크 모음, 취업 팁, 광고, 동아리/학회/스터디 면접, 노이즈

## 실행 예시

이미 알고 있는 URL만 실사:

```bash
python -m pipeline.data_audit.audit --provider none --seed-url "https://example.com/post"
```

Naver Search API 사용:

```bash
python -m pipeline.data_audit.audit --provider naver --max-results-per-query 30 --fetch-limit 200
```

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

결과는 기본적으로 `pipeline/data_audit/reports/`에 저장됩니다.

## 산출물

- `audit_report.json`: 전체 결과와 질문 후보를 담은 JSON
- `audit_report.md`: 사람이 검수하기 좋은 요약 리포트
- `gpt_manual_review_prompt.md`: ChatGPT에 붙여넣어 A등급 후보를 수동 재분류하기 위한 프롬프트

## 판단 기준 제안

- 최근 2년 기준 `A` 문서가 100개 이상이면 "최신 실제 면접 후기 기반 RAG"를 메인으로 밀 수 있음
- `A` 문서가 30~100개면 실제 후기 + 질문 은행 + 채용/기술 트렌드 보강형 RAG가 현실적
- `A` 문서가 30개 미만이면 실제 후기 크롤링은 보조 기능으로 두고, 이력서 기반 질문 생성 중심으로 전환 권장

## Tistory가 Naver API에서 적게 잡히는 이유

Naver 검색 API의 `blog` 타겟은 **blog.naver.com 전용**이고, `webkr` 타겟은 한국 전체 웹 문서를 반환하지만 tistory 비중이 낮습니다.
Tistory는 구글 검색에 더 잘 노출되므로 `--provider tistory`, `--provider google`, `--provider multi`를 사용하면 tistory 문서를 훨씬 많이 수집할 수 있습니다.

## 현재 실사에서 드러난 주의점

- 공개 웹에는 실제 질문이 여러 개 적힌 후기가 있긴 하지만, 광고/가이드/질문은행/회고 문장이 많이 섞입니다.
- 규칙 기반 분류만으로는 A등급이 과대평가될 수 있습니다.
- 실제 KB 업로드 전에는 `gpt_manual_review_prompt.md`를 ChatGPT에 붙여넣어 "실제 기업 면접 후기인지", "백엔드 기술 질문만 추출됐는지"를 수동 검수하는 편이 안전합니다.
