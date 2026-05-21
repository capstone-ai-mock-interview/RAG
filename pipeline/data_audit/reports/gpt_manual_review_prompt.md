# ChatGPT 수동 검수 프롬프트

아래 후보들은 규칙 기반 크롤링 실사에서 A등급으로 분류된 문서입니다.
AI 모의면접 RAG Knowledge Base에 넣을 수 있는지 A/B/C/D로 재분류해주세요.

등급 기준:
- A: 실제 기업 면접 후기이며, 실제로 받은 개발 직무/CS 기술 질문이 3개 이상 있음
- B: 실제 기업 면접 후기지만 질문이 적거나, 회사/개인 프로젝트 맥락이 강해 일반화가 어려움
- C: 실제 후기는 아니지만 개발 직무 기술면접 질문 은행/가이드로 보조 활용 가능
- D: 광고, 강의/멘토링 홍보, 동아리/부트캠프 면접, 개인 회고/답변문, 비기술 질문, 노이즈

주의:
- 자기소개, 지원동기, 마지막 질문, 회사 위치/조직 관련 질문은 개발 직무 기술 질문으로 세지 마세요.
- 답변/회고 문장은 질문으로 세지 마세요.
- 특정 회사 내부 시스템에 지나치게 묶인 질문은 B로 낮춰주세요.
- GitHub 질문은행, 강의 페이지, 멘토링 홍보, 취업 가이드는 A가 될 수 없습니다.

아래 JSON 형식으로만 답해주세요:

```json
{
  "summary": {
    "usable_a_count": 0,
    "recommendation": "실제 후기 기반 RAG를 메인으로 써도 되는지에 대한 짧은 판단"
  },
  "items": [
    {
      "index": 1,
      "grade": "A|B|C|D",
      "reason": "짧은 이유",
      "roles": ["backend|frontend|devops_infra|ai_ml_data|cs_common|unknown"],
      "usable_questions": ["실제로 쓸 수 있는 개발 직무/CS 기술 질문만"]
    }
  ]
}
```

검수 대상:

## 1. 백엔드 개발자 [면접/학습내용]

- URL: https://velog.io/@minsgy/%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%ED%95%99%EC%8A%B5%EB%82%B4%EC%9A%A9
- Source: velog
- Roles: ['unknown']
- Published: 2021-01-07
- Freshness: old
- Rule score: 110
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 일반적으로 설명하는 DNS Lookup은 루트 도메인서버에서부터 서브도메인 서버순으로 찾게됩니다
  - TCP와 UDP의 차이점에 대해서 설명해보세요
  - TCP 3, 4 way handshake에 대해서 설명해보세요
  - TCP를 공부하셨다면 이 정도는 알겠지 하고 묻는 문제고, 실제 면접자리에서는 보통 네트워크에 대해서 설명할 때, 직접 설명하는 편입니다
  - HTTP와 HTTPS의 차이점에 대해서 설명해보세요

## 2. [diary] 프론트엔드 신입 면접 준비하기

- URL: https://velog.io/@phrygia/2022-03-09-interview
- Source: velog
- Roles: ['frontend', 'backend', 'cs_common', 'ai_ml_data']
- Published: 2023-01-18
- Freshness: recent
- Rule score: 102
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - HTTP란 뭔가요?
  - REST API란 무엇인가요?
  - 브라우저 렌더링 과정을 설명해주세요
  - → 설명 후, CSSOM의 작동원리는 뭔가요?
  - CORS란 뭔가요?

## 3. 2025년 이직 회고 (숨고 최종합격)

- URL: https://velog.io/@cdw8431/2025%EB%85%84-%EC%9D%B4%EC%A7%81-%ED%9A%8C%EA%B3%A0-%EC%88%A8%EA%B3%A0-%EC%B5%9C%EC%A2%85%ED%95%A9%EA%B2%A9
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra', 'frontend']
- Published: 2025-05-28
- Freshness: recent
- Rule score: 94
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 예를 들어, ECS 기반의 인프라 재구성, 웹뷰 시스템을 Next.js로 전환하는 등의 작업을 통해 백엔드뿐만 아니라 인프라와 프론트엔드 영역까지 경험을 넓힐 수 있었다
  - 물론 백엔드 측면에서도 PHP 기반의 레거시 시스템을 Python + FastAPI로 마이그레이션하거나, 신규 서비스의 백엔드를 처음부터 런칭까지 주도하는 등, 스타트업에서 경험할 수 있는 기회는 밀도 있게 쌓아왔다
  - 내가 주로 다루는 언어가 Python과 PHP인데 그 때문인지 JVM을 메인으로 사용하는 포지션은 모두 서류 탈락을 경험했다
  - 과제 내용은 생각했던 것과는 큰 차이가 있었는데 서비스 스쿼드이다 보니 API를 구현하는 내용일 것이라고 예상했지만 난이도 있는 기능을 구현하는 데 초점이 맞춰져 있었다
  - 그래서 레디스를 사용한 경험이 있다고 답변을 드렸는데, 레디스가 NoSQL DB가 아니라고 하셨다

## 4. 자바 백엔드 4년차 N사 경력 면접 후기(부제 : 면접을 이끄는 건 누구인가?)

- URL: https://jeong-pro.tistory.com/240
- Source: tistory
- Roles: ['backend', 'cs_common', 'frontend', 'devops_infra', 'ai_ml_data']
- Published: 2021-09-08T23:39:41+09:00
- Freshness: old
- Rule score: 93
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 자바 백엔드 4년차 N사 경력 면접 후기(부제 : 면접을 이끄는 건 누구인가?
  - 자바 백엔드 4년차 N사 경력 면접 후기(부제 : 면접을 이끄는 건 누구인가?
  - 예를 들면 JPA N+1문제 발생 원인부터 해결 방법이라든지, 대용량 트래픽에 대한 주요 대응 방법과 특징(장단점)이라든지 하는 것들 말이다
  - 그래서 전 직장에서 프로토콜 변경하고 자료 구조 조금 바꿔서 네트워크 페이로드 크기를 줄여서 약간의 성능 개선 경험을 말해버렸다
  - 전 직장에서의 경험이라 오래되기도 하고 그렇게 드라마틱한 성과도 아닐 뿐더러 일반적인 서비스를 제공하는 회사가 경험하는 내용(프레임워크, DB, 캐시 관련된 트러블슈팅 경험, 설계 경험 등)도 아니었다

## 5. 첫 파이썬 백엔드 개발자 면접

- URL: https://inmonim.github.io/posts/first-startup-interview-sseol/
- Source: inmonim.github.io
- Roles: ['devops_infra', 'cs_common', 'backend', 'ai_ml_data', 'frontend']
- Published: 2024-12-16T04:35:00+09:00
- Freshness: recent
- Rule score: 92
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 파이썬 3.13 버전을 써봤다고 했는데, 어떻게 썼는가?
  - Flask, FastAPI, Django 수준으로 설명했다
  - Django를 활용해 어드민 시스템을 개발하여 프론트엔드 팀원들이 쉽게 쓸 수 있도록 만든 경험이 있다
  - Django ORM과 SQLAlchemy 중 무엇을 더 선호하는가?
  - Github actions, AWS ECR, Docker로 CI/CD를 구축했다고 했는데, 프로세스를 설명해달라

## 6. 신입 백엔드 면접 질문 Ver. 2.0.7

- URL: https://velog.io/@yukina1418/%EC%B5%9C%EA%B7%BC-%EB%A9%B4%EC%A0%91%EC%9D%84-%EB%8B%A4%EB%8B%88%EB%A9%B4%EC%84%9C-%EB%B0%9B%EC%95%98%EB%8D%98-%EC%A7%88%EB%AC%B8%EB%93%A4
- Source: velog
- Roles: ['unknown']
- Published: 2022-06-29
- Freshness: old
- Rule score: 92
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - In-memory DB에 대해서 설명해주세요
  - Redis를 사용하신 이유가 무엇인가요?
  - Redis와 Memcached의 차이를 이야기해주세요
  - Redis를 비전공자에게 설명해준다고 생각하고 이야기해주세요
  - Redis의 단점은 무엇이 있을까요?

## 7. 개발자 경력직 기술면접, 준비, 뒤늦은 후기

- URL: https://mellowp-dev.tistory.com/4
- Source: tistory
- Roles: ['unknown']
- Published: 2019-10-03T15:00:33+09:00
- Freshness: old
- Rule score: 88
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 알고리즘 관련해서 정리를 잘해놓은 블로그가 많아 공부하기 편했고, 코딩 테스트를 해볼수 있는 사이트에서 실전(?) 도 여러번
  - 추가로 과제에서 JPA 를 사용할 계획이 있는지, TDD 코드도 추가 할건지 ?
  - H2 DB 를 사용할건지 ?
  - 타 팀과 연동작업을 할때 API 문서는 어떤식으로 작성하고 관리 했는지를 물어보았다
  - 위와 같이 경험했던 내용을 말했고,  swagger 를 사용할때가 개인적으로 좋았다고 말씀드리며 기회가 되면 Spring Rest Docs 도 해보고 싶다고 나름 어필(?) 하였다

## 8. [면접] Spring 및 백엔드 질문리스트

- URL: https://velog.io/@tjddnths0223/%EB%A9%B4%EC%A0%91-Spring-%EB%B0%8F-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%A7%88%EB%AC%B8%EB%A6%AC%EC%8A%A4%ED%8A%B8
- Source: velog
- Roles: ['unknown']
- Published: 2022-10-11
- Freshness: old
- Rule score: 88
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JPA는 무엇인가
  - 그리고 객체지향 프로그래밍은 클래스를 사용하고 RDBMS는 테이블을 사용하는데 이 모델 간에 불일치가 존재하는데, 이런 패러다임 불일치를 해결해준다
  - Spring Framework와 Spring Boot의 차이
  - Spring Web MVC의 Dispatcher Servlet 동작원리
  - Spring Bean Life Cycle에 대한 설명

## 9. 백엔드 면접 질문 따라써보기 TIL(3)

- URL: https://velog.io/@ljh95/%EB%B0%B1%EC%97%94%EB%93%9C-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EB%94%B0%EB%9D%BC%EC%8D%A8%EB%B3%B4%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'frontend', 'ai_ml_data', 'devops_infra']
- Published: 2021-02-09
- Freshness: old
- Rule score: 86
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 일반적으로 설명하는 DNS Lookup은 루트 도메인 서버 에서부터 서브 도메인 서버 순으로 찾게 됩니다
  - TCP와 UDP의 차이점에 대해서 설명해보세요
  - RTP는 빠른 전송 기능을 지우너하기 위해 UDP프로토콜위에서 구현되엉 ㅣㅅ으며, 데이터 그램의 분실이나 도착순서 변경등의 오류를 RTP에서 해결하는 구조로 이루어져있다
  - +) TCP와 UDP 헤더의 차이
  - TCP 3, 4 way handshake에 대해서 설명해보세요

## 10. 직접 경험하며 질문 받은 기술면접 질문 모음

- URL: https://velog.io/@alskt0419/%EC%A7%81%EC%A0%91-%EA%B2%BD%ED%97%98%ED%95%98%EB%A9%B0-%EC%A7%88%EB%AC%B8-%EB%B0%9B%EC%9D%80-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EB%AA%A8%EC%9D%8C
- Source: velog
- Roles: ['frontend', 'backend', 'cs_common', 'devops_infra', 'ai_ml_data']
- Published: 2020-12-06
- Freshness: old
- Rule score: 85
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - typescript를 사용한 이유가 무엇이고 사용했을때 장점이 뭔가요?
  - Rest api에 대해 설명해 주세요
  - HTTP 메서드가 무엇인가요?
  - 본인이 알고 있는 자료구조를 있는 대로 설명해주세요
  - 자료구조를 실무에서 사용한 사례가 있나요?

## 11. 28세 요우의 개발자 이직 대탐험

- URL: https://luckyyowu.tistory.com/382
- Source: tistory
- Roles: ['backend', 'ai_ml_data', 'frontend', 'cs_common', 'devops_infra']
- Published: 2018-02-20T02:57:58+09:00
- Freshness: old
- Rule score: 83
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 경험이 전무 했던 GCP + Java Servlet 기술 스택이었습니다
  - java가 메인인데 java 관련 경험이 없어도 크게 걱정하지 않으셨습니다
  - CTO분이 설명해준 다음 레벨 인프라 아키텍쳐가 굉장히 합리적으로 보였고, 직접 개발해보고 싶다는 생각이 많이 들었습니다
  - 대규모 글로벌 트래픽과 고도화된 AWS 인프라 스펙을 경험할 수 있다는 점이 매혹적이었습니다
  - 과제를 제출했고, 어차피 인생 첫 스프링 프로젝트라 퀄리티 보다는 프로젝트를 어떻게 진행하고 이슈 해결을 위해 어떻게 접근했는지를 상세히 기록해서 추가 제출했습니다

## 12. [SW마에스트로 15기]얻은 것이 많은 심층 면접 탈락자의 회고

- URL: https://velog.io/@alswp006/SW%EB%A7%88%EC%97%90%EC%8A%A4%ED%8A%B8%EB%A1%9C-15%EA%B8%B0%EC%96%BB%EC%9D%80-%EA%B2%83%EC%9D%B4-%EB%A7%8E%EC%9D%80-%EC%8B%AC%EC%B8%B5-%EB%A9%B4%EC%A0%91-%ED%83%88%EB%9D%BD%EC%9E%90%EC%9D%98-%ED%9A%8C%EA%B3%A0
- Source: velog
- Roles: ['unknown']
- Published: 2024-03-22
- Freshness: recent
- Rule score: 83
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 크롬 확장 프로그램은 불편함을 개선하기 위해 만들었고 성공적으로 배포까지 해보았다는 것을 적었고 알고리즘 스터디는 제가 직접 만들어 스터디 계획, 스터디 과정을 그렇게 계획한 이유를 차근차근 설명하며 적었습니다
  - 생활 속에서 문제를 해결하기 위해 알고리즘 적용해본 사례가 있는지?
  - RESTful API란?
  - RESTful API의 장단점
  - REST API 종류?

## 13. 신촌 연합 IT 창업 동아리, CEOS 19기 서류, 면접 합격 후기 (백엔드)

- URL: https://blog.everdu.com/293
- Source: blog.everdu.com
- Roles: ['backend', 'cs_common', 'frontend', 'devops_infra', 'ai_ml_data']
- Published: 2024-03-03T23:30:49+09:00
- Freshness: recent
- Rule score: 82
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 이 흐름으로 경험을 구체적으로 서술하면서 '알고리즘 분야에 대한 성장 욕구' 를 어필하고자 했다
  - : GitHub 링크를 포함하여 개발 경험이나 역량을 보여줄 수 있는 링크를 첨부해 주세요
  - 그래서 이번 방학때 JPA를 공부하며 흥미가 생겼으나 원리를 몰라서 답답했는데, 이 스터디를 통해 원리를 공부할 수 있어서 기대된다고 답했다
  - 앞에서 말한대로 JPA 활용만을 해보았으므로 원리 공부를 하지 않아 부정확할 수 있다는 밑밥?을 깔았다
  - [개인] SQL 과 JPQL 의 차이점을 말해주세요

## 14. 8월 캠프콘 후기 : 기술 면접관이 알려주는 백엔드 기술 면접 합격 A to Z

- URL: https://velog.io/@socra/8%EC%9B%94-%EC%BA%A0%ED%94%84%EC%BD%98-%ED%9B%84%EA%B8%B0-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91%EA%B4%80%EC%9D%B4-%EC%95%8C%EB%A0%A4%EC%A3%BC%EB%8A%94-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%ED%95%A9%EA%B2%A9-A-to-Z
- Source: velog
- Roles: ['unknown']
- Published: 2024-08-31
- Freshness: recent
- Rule score: 81
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드 개발이란?
  - 백엔드 개발자는 Application이 어떻게 데이터를 처리하고, 사용하는지 가장 잘 알고 있습니다
  - 💡 데이터베이스의 인덱스에 대해 설명해주세요
  - 모호한 문제 설명, 비체계적인 접근: 한 번 서버가 느려진 적이 있었는데, 원인을 찾기가 어려웠어요
  - 결국엔 서버를 재시작했더니 문제가 해결됐습니다

## 15. [11월 면접 & 코딩테스트 후기]

- URL: https://velog.io/@sdj3261/11%EC%9B%94-%EB%A9%B4%EC%A0%91-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'devops_infra', 'ai_ml_data', 'cs_common', 'frontend']
- Published: 2021-12-03
- Freshness: old
- Rule score: 81
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 웹 프론트엔드 쪽이 많은데 백엔드 지원한 이유?
  - NOSQL 디비를 설계하실때 가장 중요시 본 관점이 있는가?
  - Docker CRIU 설명 -> Criu 원리 왜 필요한지 에 대해서 설명 좋아하신거 같다
  - HTTPS 무료 인증서 어떤거를 사용하셨는지?
  - Git Commit / Merge 시 충돌 문제 안 일어 났는가?

## 16. [면접총정리] 신입 개발자 인터뷰 대비 총정리 자료 - ⑤ 운영체제

- URL: https://hoons-dev.tistory.com/95
- Source: tistory
- Roles: ['unknown']
- Published: 2022-10-31T14:38:50+09:00
- Freshness: old
- Rule score: 80
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Java 를 사용하지 않는다면, 자신의 직무 언어 및 프레임워크 관점에서 문제를 해결해보는 것을 추천합니다
  - 💡 OS(운영체제)가 무엇인지 설명해주실 수 있나요?
  - + 동기화가 무엇인지 Java 챕터에서 참고
  - 💡 Race Condition과 Critical Section이 무엇이고, 경쟁상태를 막기 위해 어떤 방법을 사용하는지 설명해주세요
  - 💡 페이지 교체가 언제 발생하는지, 어떤 교체 알고리즘이 있는지 설명해주세요

## 17. [실제 면접 질문] 강남 소재 IT 중소기업 백엔드 경력직 면접 후기 - 솔루션 업체

- URL: https://back.tistory.com/44
- Source: tistory
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'frontend', 'devops_infra']
- Published: 2022-03-08T10:12:41+09:00
- Freshness: old
- Rule score: 78
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - Q) K.자바 버전은 뭘 쓰셨죠?
  - Q) K.Java8의 장점이나 특성을 설명해주세요
  - 만드셨던 RestAPI에서 각 URL은 어떤 기능들이 있었어요?
  - Q) K.Http 메소드 아는 대로 설명해주세요
  - Q) K.SpringFramework, SpringBoot , Spring에 대해 아는 대로 설명해주세요

## 18. 백엔드 개발자 기술 면접 후기

- URL: https://notspoon.tistory.com/32
- Source: tistory
- Roles: ['backend', 'cs_common', 'frontend']
- Published: 2022-08-06T20:22:23+09:00
- Freshness: old
- Rule score: 76
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - API개발을 하면서 신경쓰는부분이 뭔가요?
  - Java에서 SQL 주입 방지 어떻게 처리?
  - Java Enum이 사용해봤는지, 왜쓰는지
  - 왜 Spring batch 썻는지
  - spring batch 관련 테이블이 무엇이 있는가

## 19. SPRING 면접 질문

- URL: https://velog.io/@winckey0/SPRING-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8
- Source: velog
- Roles: ['unknown']
- Published: 2022-11-07
- Freshness: old
- Rule score: 76
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 스프링에서 AOP가 뭔가요?
  - MVC에 대해서 설명해주세요
  - JPQL에서 동작한 쿼리를 통해서 members에 데이터가 바인딩 됩니다
  - 이미 영속성 컨텍스트에 들어있기 때문에 따로 쿼리가 실행되지 않은 채로 N+1문제가 해결됨
  - 자바 컬렉션 List, set, map에 대한 설명

## 20. 면접대비- 인성,기술 대비

- URL: https://velog.io/@sog3152/%EB%A9%B4%EC%A0%91%EB%8C%80%EB%B9%84-1
- Source: velog
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'frontend']
- Published: 2023-03-21
- Freshness: recent
- Rule score: 76
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 롤모델이 있다면 누구고 그 이유는?
  - 재밌게 공부한 알고리즘이 있다면?
  - 좋아하는 자료구조가 있다면?
  - 위에서 좋아하는 자료구조를 설명할 때 얘기했음!
  - 인덱스랑 무엇이고 일반적인 원리는 어떠한가?

## 21. 백엔드 면접 질문 정리(update - 20.04.19) | Junjangsee's Blog

- URL: https://junjangsee.github.io/2019/05/15/interview/interview/
- Source: junjangsee.github.io
- Roles: ['backend', 'cs_common', 'ai_ml_data']
- Published: 2019-05-15
- Freshness: old
- Rule score: 75
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 오버로딩(Overloading)과 오버라이딩(Overriding)의 차이
  - 스프링 프레임워크(Spring Framework)란?
  - DI(의존성 주입)란?
  - Spring과 SpringBoot의 차이
  - 오버로딩(Overloading)과 오버라이딩(Overriding)의 차이

## 22. 위코드 수료 후 백엔드 면접 후기 및 FAQ1 - 기술면접 · Lunallena TIL Blog

- URL: https://lunayyko.github.io/wecode/2021/10/27/interview1/
- Source: lunayyko.github.io
- Roles: ['unknown']
- Published: None
- Freshness: unknown
- Rule score: 75
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JWT는 무엇인가?
  - JWT를 왜 사용하였는지?
  - JWT의 변조 알고리즘에는 무엇이 있는지?
  - JWT가 어떤 방식의 해킹을 당할 수 있는지 그리고 그걸 예방하기 위해서 어떻게 해야하는지?
  - Eager Loading은 무엇인가?

## 23. 신입 프론트엔드 개발자로 취업하기(면접 정리)

- URL: https://velog.io/@jiaeyamm33/%EC%8B%A0%EC%9E%85-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A1%9C-%EC%B7%A8%EC%97%85%ED%95%98%EA%B8%B0%EB%A9%B4%EC%A0%91-%EC%A0%95%EB%A6%AC
- Source: velog
- Roles: ['frontend', 'cs_common', 'backend', 'ai_ml_data']
- Published: 2023-07-23
- Freshness: recent
- Rule score: 74
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - http란 무엇인가?
  - http 통신 요청에 대한 결과값에 대해 아는가?
  - RESTful API란?
  - 리액트 인강을 듣는다고 했는데 최근 배운 게 무엇인가?
  - 리액트 쿼리랑 axios의 차이점?

## 24. 신입 백엔드 개발자 추천 프로젝트 7선과 실전 팁 - 코딩취업아카데미

- URL: https://keduitcenter.co.kr/%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B6%94%EC%B2%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-7%EC%84%A0%EA%B3%BC-%EC%8B%A4%EC%A0%84-%ED%8C%81/
- Source: keduitcenter.co.kr
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'devops_infra', 'frontend']
- Published: 2025-08-16T22:47:19+00:00
- Freshness: recent
- Rule score: 68
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 쇼핑몰 구축: 데이터베이스 설계와 결제 모듈 경험을 쌓을 수 있습니다
  - 면접관의 65%는 프로젝트 설명 능력을 평가하며, GitHub 커밋 빈도가 높은 프로젝트가 합격률을 20% 이상 높인다는 데이터도 있습니다(출처: IT 취업 전문가 2023, 사람인 2024, 원티드 2024, 2023년 데이터 분석
  - 사람인 조사에서도 프로젝트 설명 부족으로 30% 이상이 감점을 받았으며, GitHub 커뮤니티 분석에 따르면 불필요한 기능 추가로 완성도가 떨어진 사례가 25%에 달합니다(출처: 잡코리아 2023, 원티드 2024, 사람인 2024, GitHub 커뮤니티 분석
  - 신입 백엔드 개발자가 처음 시작하기 좋은 프로젝트 주제는 무엇인가요?
  - 최신 백엔드 프로젝트에 추천되는 기술 스택은 무엇인가요?

## 25. [소프트웨어 마에스트로 13기] 포트폴리오 & 심층 면접 & 최종 합격 후기

- URL: https://velog.io/@jsb100800/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4-%EB%A7%88%EC%97%90%EC%8A%A4%ED%8A%B8%EB%A1%9C-13%EA%B8%B0-%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4-%EC%8B%AC%EC%B8%B5-%EB%A9%B4%EC%A0%91-%EC%B5%9C%EC%A2%85-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra', 'frontend']
- Published: 2022-04-08
- Freshness: old
- Rule score: 68
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 다양한 기술 스택에서 공부해본 경험이 있으며, 현재는 백엔드 분야의 매력을 느껴서 백엔드 개발자가 되기 위해 노력하고 있다
  - 내가 느꼈다고 했던 백엔드의 매력 이 무엇인지 자세히 설명해달라는 질문을 받았다
  - 리액트 하면서 어려운점이 있었나?
  - 스프링 관련,, 스프링에서 뭐해봤는지 구체적인 설명
  - 왜 스프링을 사용했나?

## 26. [면접총정리] 신입 개발자 인터뷰 대비 총정리 자료 - ① 자료구조

- URL: https://hoons-dev.tistory.com/91
- Source: tistory
- Roles: ['backend', 'cs_common', 'frontend', 'ai_ml_data', 'devops_infra']
- Published: 2022-12-18T21:03:34+09:00
- Freshness: old
- Rule score: 65
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - Java 를 사용하지 않는다면, 자신의 직무 언어 및 프레임워크 관점에서 문제를 해결해보는 것을 추천합니다
  - 고정길이, 느린 삽입 삭제 연산을 해결하기 위해서 나온 자료구조가 바로 LinkedList 입니다
  - [🧪 컴퓨터과학 : CS] - [자료구조] Array와 LinkedList의 차이 (인터뷰 대비
  - [자료구조] Array와 LinkedList의 차이 (인터뷰 대비
  - 💡  + Java 의 Collections 에 대해서 알고 있나요?

## 27. 백엔드 개발자 면접 질문 정리

- URL: https://parksunwoo.github.io/dev/2023/01/01/backend-engineer-interview-question.html
- Source: parksunwoo.github.io
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra', 'frontend']
- Published: 2023-01-01T00:00:00+00:00
- Freshness: recent
- Rule score: 64
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 인덱스란 무엇인가?
  - 이 문제 해결방식으로 Eeger-Loading 방식이 있다
  - ‘https://example.com/api/users?version=v1’
  - 아키텍처적인 결정을 왜 그렇게 내렸는지 코드 베이스안에 기록해 놓는 것.GitHub은 iOS/Android 모바일팀에서 이걸 적용하고 있으며, 왜 필요한지를 설명한 글
  - 진짜 보너스는 누군가 몇달후에 왜 GitHubAPIClient 모듈이 이렇게 동작하는지 당신을 비난하면서 물어볼 때 나타남.30분 페어링해서 코드를 설명하는 것 보다, 이 ADR을 던져주고 그 모듈을 빌드하는 동안 내린 결정에 대해 설명할 수 있게 됨

## 28. 프로그래머스 백엔드 데브코스 4기 합격 후기

- URL: https://changhyeon-h.tistory.com/21
- Source: tistory
- Roles: ['backend', 'frontend', 'cs_common', 'ai_ml_data']
- Published: 2023-06-24T21:52:10+09:00
- Freshness: recent
- Rule score: 63
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 기술면접에서 자바스크립트의 동작원리 , 싱글톤이 무엇인지 설명해주세요 와 같은 답이 명확하게 나오는 질문들을 준비했었지만 면접관님께서 질의해주신 내용은 명확한 답이 나오는 질문이 아닌 문제를 주고 스스로 생각해서 해결 할 수 있는 그러한 문제들을 내주셨던 것 같아요
  - 수학적인 지식들도 여쭤보셨었고 SNS DB를 설계해보고 설명해달라고도 하셨었습니다
  - 웹 백엔드 분야로 진출하고자 결심한 이유는 무엇인가요?
  - 웹 백엔드 진로를 위해 그동안 노력해온 것이 있나요?
  - 데브코스에서 어떻게 학습을 이어갈 계획인가요?

## 29. NHN Bugs 에서 버벅된 솔직 후기

- URL: https://velog.io/@albon/NHN-Bugs-%EB%A9%B4%EC%A0%91%EC%97%90%EC%84%9C-%EB%B2%84%EB%B2%85%EB%90%9C-%EC%86%94%EC%A7%81-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2026-02-12
- Freshness: recent
- Rule score: 62
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - Redis, Kafka, 문제 해결에 대한 내용을 엄청 공부해서 면접장에 갔지만 해당 문제과 질문이 전혀 나오지 않아 아쉬울 따름입니다
  - MSA 구조와 Kafka, Redis 기반의 비동기 아키텍처 중심으로 학습을 진행하다 보니 서비스 내부의 Multi Thread 동작 원리나 전통적인 동시성 처리에 대한 질문이 나올 것이라는 부분까지는 충분히 생각하지 못했던 점이 아쉬웠습니다
  - 평소 알고리즘을 꾸준히 정리해두었다면 문제 유형만 보고도 개선 방향을 빠르게 도출할 수 있었을 텐데 실전에서 바로 연결하지 못한 점이 아쉬웠고 앞으로는 실무 중심뿐 아니라 알고리즘적 사고와 문제 해결 패턴도 함께 보완해야겠다고 느꼈습니다
  - 이번 경험을 계기로 CS 기본기를 더욱 탄탄히 다질 필요성을 느꼈고 앞으로는 CS를 기반으로 한 학습을 꾸준히 이어갈 예정입니다

## 30. 엘리스 면접 특강을 돌아보며 (feat. 백엔드)

- URL: https://velog.io/@malza_0408/%EC%97%98%EB%A6%AC%EC%8A%A4-%EB%A9%B4%EC%A0%91-%ED%8A%B9%EA%B0%95%EC%9D%84-%EB%8F%8C%EC%95%84%EB%B3%B4%EB%A9%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-08-14
- Freshness: old
- Rule score: 61
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 멱등성을 보장하는 REST method?
  - 🔥✅ HTTP와 HTTPS의 차이?
  - 🔥✅ HTTP를 사용하는 REST API 서버에게 HTTPS를 사용하게 하기 위해서는 어떠한 절차를 거쳐야 하는지?
  - HTTP -> TCP -> 패킷의 흐름까지 이해하고 설명 할 수 있으면 훌륭하다
  - HTTP 연결을 맺을 때 수행되는 TCP Three-way-handshake와 HTTPS 연결을 맺을 때 수행되는 TLS handshake를 설명할 수 있으면 좋다

## 31. [SKT Devocean Young] JPA 도서 스터디 후기

- URL: https://velog.io/@jiww4/SKT-Devocean-Young-JPA-%EB%8F%84%EC%84%9C-%EC%8A%A4%ED%84%B0%EB%94%94-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2024-11-30
- Freshness: recent
- Rule score: 61
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JPA란 JPA(Java Persistence API)는 자바 개발자에게 객체와 관계형 데이터베이스 간의 매핑을 지원하는 ORM 기술 표준으로, 애플리케이션과 JDBC 사이에서 동작
  - +) ORM(Object-Relational Mapping) 객체와 관계형 데이터베이스 간의 패러다임 불일치를 해결하기 위해 객체와 테이블을 매핑하며, JPA는 SQL 작성 및 변환 작업을 대신 처리해 개발자의 부담을 줄임
  - JPA의 간단한 동작 원리객체 저장 시 SQL을 자동 생성하여 데이터베이스에 저장하고, 조회 시 객체 그래프를 탐색하며 필요한 데이터를 적절히 조회
  - H2 오류 해결H2 데이터베이스를 사용할 경우, 파일 경로(예: Users/user/test test.mv.db)가 올바르게 설정되어 있는지 확인
  - 플러시와 트랜잭션플러시는 영속성 컨텍스트의 변경 내용을 데이터베이스에 반영하며, 트랜잭션 커밋, JPQL 실행, flush() 호출 시 동작

## 32. 다우데이타 현장 실습 면접

- URL: https://velog.io/@gmlstjq123/%EB%8B%A4%EC%9A%B0%EB%8D%B0%EC%9D%B4%ED%83%80-%ED%98%84%EC%9E%A5-%EC%8B%A4%EC%8A%B5-%EB%A9%B4%EC%A0%91
- Source: velog
- Roles: ['backend', 'cs_common', 'devops_infra', 'ai_ml_data', 'frontend']
- Published: 2023-12-18
- Freshness: recent
- Rule score: 61
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - ③-a 경력사항에 AWS 온라인 교육을 받은 게 있는데, 여기에서 무엇을 배웠나요?
  - AWS에서 제공하는 서비스의 종류, 클라우드 컴퓨팅 관련 용어와 필요성, 동작 원리에 대한 설명을 들을 수 있었습니다
  - ③-b 구체적으로 어떤 AWS 서비스를 사용했나요?
  - ③-c AWS 기술을 적용하는 과정에서 어려움은 없었나요?
  - ④ 백엔드 개발할 때, Spring 말고 Node.js는 안 써보셨어요?

## 33. 백엔드 개발자 경력(3년차) 면접 질문 및 코테 후기

- URL: https://roajava.tistory.com/270
- Source: tistory
- Roles: ['backend', 'frontend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2026-03-10T15:02:18+09:00
- Freshness: recent
- Rule score: 59
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 거기에서 DB 성능을 위해 어떠한 노력을 해보았는지?
  - PostgreSQL은 사용해본적 없는지?
  - WAS와 웹 서버의 차이점
  - Spring에서 Bean이란 무엇이며 어떤 용도로 사용되는지?
  - IoC에 대해서 설명

## 34. [면접후기] 8/30 매칭데이

- URL: https://velog.io/@hjh3933/%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0-830-%EB%A7%A4%EC%B9%AD%EB%8D%B0%EC%9D%B4
- Source: velog
- Roles: ['unknown']
- Published: 2024-09-02
- Freshness: recent
- Rule score: 59
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 질문: restful api에 대해 설명해달라고 하심
  - 질문: 입사하면 고객처에 서버 설치도 해야하는데 할 수 있는지?
  - 질문: node.js랑 spring중에 뭐가 더 자신있는지?
  - 질문: 데이터베이스 설계 해본 경험 있는지?
  - 회사 스택을 찾아보고 미리 검색하고 가는게 도움이 많이 되었음, 사실 nest.js로 이번에 처음 들었는데 node.js 관련 프레임워크라고 해서 아하 그렇구나 하고 알고 갔더니 nest.js로 사용해본적 있냐는 질문에 사용경험은 없지만 node.js를 많이 사용해보아서 금방 익힐 수 있을 것 같다고 답변할 수 있었음

## 35. 안드로이드 개발자 면접 후기 3탄

- URL: https://haenarashin.github.io/android,/career/2022/05/22/Getting_new_job.html
- Source: haenarashin.github.io
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'frontend']
- Published: 2022-05-22T12:49:00+00:00
- Freshness: old
- Rule score: 58
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - RxJava에서 flatMap과 switchMap의 차이가 무엇인가요?
  - Fragment의 lifecycleOwner로 this, view.lifecycleOwner의 차이를 설명해주세요
  - Java에서 checked exception을 왜 Kotlin에서는 사용하지 않았을까요?
  - git merge와 rebase의 차이와 각각을 언제 사용하나요?
  - 가령 예를 들면 HTTTPS vs HTTP의 차이 는 어느 회사든 나올법한 질문이지만 그 대답에 이어 그럼 그 SSL Handshaking이 어떻게 진행되는지도 설명 가능할까요?

## 36. [면접] 기술면접 질문 및 후기 정리

- URL: https://esther99.tistory.com/44
- Source: tistory
- Roles: ['unknown']
- Published: 2024-04-09T16:41:13+09:00
- Freshness: recent
- Rule score: 58
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JPA와 Querydsl은 명확한 차이가 있을텐데 어떤 차이가 있고, 어떤 점이 좋았는지?
  - 백엔드를 선택한 이유는?
  - HTTP에서 get과 post 통신의 차이를 아는지?

## 37. 2025년 하나은행 상반기 최종합격 후기 (디지털/ICT)

- URL: https://velog.io/@devwoong/2025%EB%85%84-%ED%95%98%EB%82%98%EC%9D%80%ED%96%89-%EC%83%81%EB%B0%98%EA%B8%B0-%EC%B5%9C%EC%A2%85%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0-%EB%94%94%EC%A7%80%ED%84%B8ICT
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2025-05-24
- Freshness: recent
- Rule score: 58
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 내 첫 인턴경험은 스마트팩토리에 필요한 기업전사관리시스템을 개발하는 일이었는데 클라우드 경험과 도메인 중심의 백엔드 개발을 하고싶어서 1년 4개월 일하던 회사에서 나와서 스타트업에 가서 새롭게 인턴쉽을 했었다
  - 첫 인턴했던 회사에서 SQL을 많이 다뤘었고 SQLD 자격증 취득한 경험이 있어서 다행히 짧은시간에 대비를 했고 알고리즘에 좀 더 집중했다
  - [링크] https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit
  - MLOps의 Continuous training 쪽을 다뤄보고 싶다고 자소서에 적어주셨는데 어떤 개념이고 왜 사용하는지?
  - [참고영상] https://www.youtube.com/watch?v=DOvCIrwMPbQ&t=880s

## 38. [현대오토에버] 2023년 1분기 신입 공채 최종 합격 후기 - 커넥티드 카 서비스(CCS)

- URL: https://heesangstudynote.tistory.com/110
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra', 'ai_ml_data']
- Published: 2024-01-06T19:26:33+09:00
- Freshness: recent
- Rule score: 56
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 예를 들어서 저는 Spring MVC 패턴에 대한 동작 원리를 깊이 있게 이해하며 사용했습니다

## 39. [기술면접] Spring 면접질문 (3)

- URL: https://velog.io/@rdamin/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-Spring-%EB%A9%B4%EC%A0%91%EC%A7%88%EB%AC%B8-3
- Source: velog
- Roles: ['unknown']
- Published: 2025-01-02
- Freshness: recent
- Rule score: 56
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - POJO란 무엇인가, Spring Framework에서 POJO는 무엇이 될 수 있을까?
  - RESTFul이란 무엇인지, 아는대로 설명하시오
  - 서버-클라이언트 구조: 서버와 클라이언트가 독립적으로 동작하며, HTTP를 통해 상호작용합니다
  - 긴급 상황에서는 우선 스케일 아웃과 캐시 적용 등 단기적인 해결책에 집중하고, 이후 장기적으로 로드 밸런서와 DB 최적화를 진행합니다
  - 어떻게 쿼리가 실행될까?

## 40. [제로베이스 취업보장 백엔드 스쿨 후기] 2년 차 개발자를 바라보며

- URL: https://velog.io/@wsh096/%EC%A0%9C%EB%A1%9C%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%B7%A8%EC%97%85%EB%B3%B4%EC%9E%A5-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%8A%A4%EC%BF%A8-%ED%9B%84%EA%B8%B0-2%EB%85%84-%EC%B0%A8-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EB%B0%94%EB%9D%BC%EB%B3%B4%EB%A9%B0
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra', 'frontend']
- Published: 2024-11-28
- Freshness: recent
- Rule score: 56
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - Q1.) 제로베이스 백엔드 스쿨을 수료하고 현재는 어떤 일을 하고 계신가요?
  - 해당 학습을 완료하거나, 완주한다면 소프트웨어 개발자 입니다.라는 어휘를 쓰지 않아도, 생각과 행동에서 이미 개발자인가?
  - 절반도 안 되는 가격에, 심지어 평생 수강할 수 있는 강의와 앞선 선배들이 개발해 둔 레퍼런스도 충분히 쌓였으며, 스스로 고민하고 해결해 나가고 구조를 이해하는 학습을 통해 더욱 빠르게 앞으로 더 많이 좋은 개발자가 될 수 있을 거라 생각합니다
  - Q3-2.) 잠시 딴 길로 샜는데 제로베이스에서 학습했던 것들을 구체적으로 다시 한 번 소개해 주시겠어요?
  - 현재는 코딩테스트를 C++로 학습하고 준비하지만, 이 모든 기준이 되는 컴퓨터적 사고의 기본은 Java를 기반으로 이해하고 Java와 차이를 따지며 분석할 수 있습니다

## 41. 2022 상반기 라인 신입 공채 후기 (코딩테스트/필기테스트/1차면접/2차면접)

- URL: https://esot3ria.github.io/programming/2022-06-20-line-test-and-interview/
- Source: esot3ria.github.io
- Roles: ['backend', 'cs_common', 'ai_ml_data']
- Published: 2022-06-20T00:00:00+00:00
- Freshness: old
- Rule score: 55
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드 개발자는 경험한 트래픽의 규모에 따라 성장하는 경향이 있습니다
  - 서버가 적은 사용자 규모에서는 문제없이 동작하더라도, 사용자가 급격히 많아지면 꼭 어느 부분에서는 문제가 생기기 마련입니다
  - 만약 얕게 경험했던 백엔드 프로젝트 위주로만 작성한다면 서류 평가 때는 유리하겠지만 정작 면접 때 경쟁력을 갖출 수 없다고 생각했기 때문입니다
  - CS의 4대 요소라고 할 수 있는 네트워크, 데이터베이스, 자료구조, 운영체제 과목 모두 골고루 돌아가며 심도 깊은 질문이 나왔고 제가 이해했던 내용을 말로 풀어 설명했습니다

## 42. 5월 12일 면접 후기

- URL: https://sharekim-dev.tistory.com/77
- Source: tistory
- Roles: ['frontend', 'backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2025-05-14T12:49:29+09:00
- Freshness: recent
- Rule score: 54
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - : CJ프레시웨이에서 서비스운영 업무를 담당할 당시에 데이터를 파이썬으로 시각화 한 경험이 있었습니다
  - 프론트엔드 기술에 대해서는 어떻게 학습하셨나요?
  - 학습한 내용을 실무에 적용하면서 겪는 문제를 해결하면서도 실력을 향상시켰던 것 같습니다
  - 면접 경험 : 3 대 1 면접으로 진행되었고, 프론트엔드에 대한 질문은 크게 없었고 개발자로서 어떤 성장을 해왔는지에 대한 질문이 이어졌다

## 43. JAVA 신입 1차 면접 질문

- URL: https://velog.io/@aleydis/JAVA-%EC%8B%A0%EC%9E%85-1%EC%B0%A8-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8
- Source: velog
- Roles: ['unknown']
- Published: 2020-09-03
- Freshness: old
- Rule score: 54
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 데이터베이스에는 어떤 테이블이 있었고, 각 테이블의 컬럼은 뭐가 있었나요?
  - 프로젝트에서 mvc 패턴을 어떻게 구성했는지
  - MVC Model1과 Model2의 차이
  - TCP/UDP 차이
  - 기억에 남는 알고리즘 문제는 무엇인가?

## 44. 3년차 백엔드 경력직 면접 후기

- URL: https://pizza7311.me/post/diary/3y-backend-interview-review
- Source: pizza7311.me
- Roles: ['backend', 'cs_common', 'devops_infra', 'frontend']
- Published: 2025-11-25
- Freshness: recent
- Rule score: 53
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 서비스중인 서버를 어떻게 무중단으로 업데이트 할것인가?
  - rdbms, noSql, redis 각각의 차이점과 어떤 상황에서 쓰는게 좋은가?
  - 이 정도 레벨이라면 솔직히 실제 프로덕션 서버를 운영하면서 스케일링이나 db마이그레이션과 같은 좀더 전문적인 경험이 있어야할 시기다
  - 전부 사내 네트워크에서만 구동이되어야하는 서비스라 클라우드를 구축하고 운영해볼 기회가 없었고 이때 나는 좀더 클라우드쪽 커리어를 희망하고있었고 계속 외주 프로젝트만 하다보면 연차만 쌓이고 실제 경험은 거의 없는 사람이 될까봐 광장히 두려운 상황이었다
  - 이러한 경험때문에 나는 백엔드 기능 개발외에 클라우드나 db관련 경험이 굉장히 적은편이다

## 45. 신입 개발자 기술면접 질문 정리 - 자바

- URL: https://velog.io/@kallis0926/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC-%EC%9E%90%EB%B0%94
- Source: velog
- Roles: ['unknown']
- Published: 2023-12-20
- Freshness: recent
- Rule score: 53
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 💡 Java의 특징을 설명해주세요
  - JVM(자바가상머신) 위에서 동작하기 때문에 운영체제에 독립적이다
  - JVM은 스택 기반으로 동작하며, Java Byte Code를 OS에 맞게 해석 해주는 역할을 하고 가비지컬렉션을 통해 자동적인 메모리 관리를 해줍니다
  - 💡 Java의 컴파일 과정에 대해 설명해주세요
  - 💡 Java에서 제공하는 원시 타입들은 무엇이 있고 각각 몇 바이트를 차지하는가?

## 46. 첫 프론트엔드 인턴 면접 후기[면접탈]

- URL: https://velog.io/@kwak1539/%ED%98%84%EC%9E%A5%EC%8B%A4%EC%8A%B5-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%9D%B8%ED%84%B4-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-11-30
- Freshness: old
- Rule score: 52
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 프론트엔드 말고도 백엔드 경험이 있는지?
  - JavaScript 말고 다른 언어를 사용해본 적이 있는지?
  - JavaScript의 Promise에 대해 설명할 수 있는지?
  - React를 사용하면서 기존 Vanilla JavaScript와 비교해서 어떤 점이 좋았는지 구체적으로 설명할 수 있는지?
  - 알고리즘 문제는 Python말고 JavaScript로는 풀어본 경험이 있는지?

## 47. 신입 개발자 기술 면접 질문 - Java

- URL: https://velog.io/@xangj0ng/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-Java
- Source: velog
- Roles: ['unknown']
- Published: 2023-02-12
- Freshness: recent
- Rule score: 52
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Java의 특징을 설명해주세요
  - JVM(자바가상머신) 위에서 동작하기 때문에 운영체제에 독립적이다
  - JVM은 스택 기반으로 동작하며, Java Byte Code를 OS에 맞게 해석 해주는 역할을 하고 가비지컬렉션을 통해 자동적인 메모리 관리를 해줍니다
  - Java의 컴파일 과정에 대해 설명해주세요
  - 불변 객체가 무엇인지 설명하고 대표적인 Java의 예시를 설명해주세요

## 48. [유튜브 영상 후기] AI 시대, 개발자로 살아가는 법

- URL: https://velog.io/@ililil9482/%ED%9B%84%EA%B8%B0-AI-%EC%8B%9C%EB%8C%80-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A1%9C-%EC%82%B4%EC%95%84%EA%B0%80%EB%8A%94-%EB%B2%95
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'frontend']
- Published: 2025-06-21
- Freshness: recent
- Rule score: 52
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 안그래도 최근 바이브 코딩을 유튜브나 링크드인에서 보면서 앞으로 내가 java 개발자로 계속 해가는게 맞을까?
  - 또 아니면 AI가 잘 사용하는 node나 python 관련된 개발을 공부해야할까?
  - 오히려 AI를 통해 문제를 풀며 문제를 해결하는 과정에 대해 질문할 수도 있고 현재의 AI의 경우 문제를 해결하는데만 치중하여 코드를 보면 문제를 고민해서 풀었다기 보다 그저 for, if와 알고리즘들을 조합하여 문제를 해결하기만 해놓은 형태가 많다
  - 이러면 java 개발자로서 위기감을 느껴야할까?
  - 백엔드 개발자로서 어디까지 알아야 할까요?

## 49. Seoul | Claude Code FDE Night 2026 세미나 후기

- URL: https://jojoldu.tistory.com/876
- Source: tistory
- Roles: ['ai_ml_data', 'backend', 'devops_infra', 'frontend', 'cs_common']
- Published: 2026-04-18T10:59:09+09:00
- Freshness: recent
- Rule score: 51
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - SI를 하겠다는 이상한(?) 스타트업 '스페이스와이' — 바이라인네트워크

## 50. [후기] 면접 후기

- URL: https://velog.io/@yaaloo/%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-06-02
- Freshness: recent
- Rule score: 51
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - MariaDB에 부분 문자열 검색 기능이 있는데, 그건 왜 거르고 ES를 사용했는가?
  - 왜냐면, jwt 자체가 약간의 보안을 희생하고 효율성을 높이기 위한 기술이기 때문에 엑세스 토큰은 저장을 하지 않고 리프레시 토큰만을 저장하게끔 설계를 했다
  - 매 요청 시마다 세션 스토리지를 조회함으로써 서버 부하를 늘리는 것이 세션 방식의 문제 중 하나인데, 매번 세션 값을 찾는거나, 사용자의 현재 jwt 값을 찾는거나 과연 다를 게...?
  - 단점은 이전 사용자를 로그아웃 시키기 위해서는 엑세스 토큰을 db에 저장해두고 매 요청마다 일치하는지 확인해야 한다는 것?
  - MariaDB에 부분 문자열 검색 기능이 있는데, 그건 왜 거르고 ES를 사용했는가?

## 51. [취준 기록] 신입 백엔드 개발자 면접 후기 (기술면접, 인성면접, 최종면접)

- URL: https://ddooroong.tistory.com/entry/%EC%B7%A8%EC%A4%80-%EA%B8%B0%EB%A1%9D-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%9D%B8%EC%84%B1%EB%A9%B4%EC%A0%91-%EC%B5%9C%EC%A2%85%EB%A9%B4%EC%A0%91
- Source: tistory
- Roles: ['unknown']
- Published: 2023-07-22T12:56:27+09:00
- Freshness: recent
- Rule score: 50
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - github에 작성한 내용 중에서) session으로 권한을 구분했다고 되어있는데, 더 자세히 설명해주세요
  - Spring 사용해보았는지?
  - Spring을 사용했을 때와 사용하지 않았을 때 본인이 느낀 점은 무엇인지?
  - 데이터베이스 프로젝트에서 테이블은 총 몇 개가 나왔는지?
  - DB 쿼리문은 잘 다루는 편인지?

## 52. [Career] 와디즈 백엔드 기술 면접 후기

- URL: https://kkang-joo.tistory.com/15
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra']
- Published: 2022-08-19T00:01:27+09:00
- Freshness: old
- Rule score: 50
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - rest api가 무엇인지 설명해보세요
  - api를 설계할 때 중요하게 생각하는 게 무엇인가 (왜 그게 중요한가, 그거 말고 응답에 ..한 경우에는 어떻게 구성할 건지
  - MSA에 대해서 설명해보세요

## 53. Consistent Developer

- URL: https://gdevblog.tistory.com/?page=7
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra', 'frontend', 'ai_ml_data']
- Published: 2021-04-18
- Freshness: old
- Rule score: 50
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 사용할 수도 있는데 이에 대해서 어떻게 생각하는지 해쉬 알고리즘이란?
  - HTTPS Node.js 자바 다른 장점 싱글 쓰레드 / 멀티 쓰레드 주로 사용하는 DB 비밀번호 관리 방법 RDBS vs NoSQL 차이점 -> 꼬

## 54. [취업] 2022 하반기 백엔드 취업회고 : 14번의 면접 그리고 취뽀 - 4 (기술면접)

- URL: https://velog.io/@rmswjdtn/%EC%B7%A8%EC%97%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%8B%A0%EC%9E%85-14%EB%B2%88%EC%9D%98-%EB%A9%B4%EC%A0%91-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%B7%A8%EB%BD%80-4-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91
- Source: velog
- Roles: ['unknown']
- Published: 2023-02-25
- Freshness: recent
- Rule score: 50
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 이 강의는 뭔가 이론적으로만 딱딱하게 배웠던 네트워크 개념을 좀더 와닿게(?) 설명해주신다
  - 면접때 Spring도 준비해야하는 분들을 위해서 공부팁을 조금 더 붙이자면 Spring의 동작원리 (?)에 대해서 깊게 이해하는 것이 좋다
  - 특히 나처럼 Spring 프로젝트 경험이 있고 그것을 서류에 썼다면 무조건 공부해야하며 다른 프레임워크를 썼던 분들은 당연히 해당 프레임워크에 대해 깊이 공부하고 가는 것이 좋다
  - 혹시 자바 스프링 학습 기간은 어느정도 되셨고 어느정도 시간을 투자하셨는지 알 수 있을까요?

## 55. Node.js 백엔드 개발자 면접후기..... (조언부탁,,) | OKKY 커뮤니티

- URL: https://okky.kr/articles/1272947
- Source: okky.kr
- Roles: ['backend', 'frontend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2022-07-14T19:04:18
- Freshness: old
- Rule score: 49
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - cto: 저의 질문의도는 레디스 말구 여러 nosql이 많은데 왜 굳이 레디스를 사용하셨나??
  -       자바스크립트가 비동기적으로 작동하자나요??
  - 자기를 어필하는거보다 질문들에 대한 개발자 다운 답변이 중요하다는것을요 ...ㅠ (자바스크립트 비동기에 대해서 간단하게 친절하게 설명해주시는 cto님 ㅠ 그리고 이어지는 면접
  - 타입스크립트 장점이 모라고 생각하시나요??
  - 불만족 하다는듯이..) 타입스크립트가 oop가 가능하자나요?

## 56. 서울 중소기업 웹 개발자 취준 후기 - 면접

- URL: https://velog.io/@iamodh/%EC%84%9C%EC%9A%B8-%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85-%EC%9B%B9-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EC%A4%80-%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91-0n5eflui
- Source: velog
- Roles: ['frontend', 'backend', 'ai_ml_data', 'cs_common']
- Published: 2025-06-16
- Freshness: recent
- Rule score: 49
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 자바스크립트의 함수 파라미터는 값에의한 호출인가요?
  - MVC 패턴에서 M은 무엇을 의미하나요?
  - 프론트엔드와 백엔드를 나누는 기준에 대해 어떻게 생각하시나요?
  - 자바스크립트의 함수 파라미터는 값에의한 호출인가요?
  - 리액트의 상태관리에 대해 설명해주세요

## 57. [취준 기록] 신입 백엔드 개발자 면접 / 기술면접 후기

- URL: https://ddooroong.tistory.com/entry/%EC%B7%A8%EC%A4%80-%EA%B8%B0%EB%A1%9D-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: tistory
- Roles: ['unknown']
- Published: 2023-07-13T12:55:02+09:00
- Freshness: recent
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 프론트엔드 / 백엔드 / 풀스텍 중에서 본인이 하고자 하는 역할은?
  - 백엔드 개발에 더 관심이 있는 이유는?
  - REST API 사용 경험
  - Spring 프로젝트에서 데이터베이스는 어떤걸 사용했는지?
  - 자바 스크립트에서 변수 var, let, const에 대해서 설명

## 58. 신입 백엔드 개발자 면접, 이렇게 질문 했습니다

- URL: https://gusrb.tistory.com/88
- Source: tistory
- Roles: ['backend', 'ai_ml_data', 'frontend']
- Published: 2025-02-16T20:54:47+09:00
- Freshness: recent
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - "객체지향의 3요소 말해보세요", "데이터베이스 트랜잭션을 아는만큼 설명하세요", "인덱스가 뭐에요?" 이런 넓은 범위의 퀴즈 성격의 질문은 지양 했다
  - 데이터베이스 트랜잭션을 깊이 아는 사람을 뽑은게 아니고, 문제 해결 과정을 경험해보고, 그 내용을 논리적으로 설명 할 수 있는 사람을 원했기 때문이다
  - "자바 잘해요?" "쿼리 잘 짜요?" 이런 잘해요?
  - 애초에 자바 잘한다의 기준이 명확 하지 않고, 실제로 잘한다 하더라도, 그 자바 지식을 어떤 문제 해결에 사용 했는지 판단 하기 어렵다

## 59. 2025 팀네이버 Tech 신입 공채 후기 (코테, 1차 면접)

- URL: https://wooing1084.tistory.com/52
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra', 'ai_ml_data']
- Published: 2025-05-30T17:19:07+09:00
- Freshness: recent
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - Git의 통신은 어떻게 동작할까?
  - Git의 통신은 어떻게 동작할까?
  - 자세한 문제 설명은 보안상 불가능하지만 풀이에 사용했던 알고리즘은 다음과 같다
  - 그 중 가장 아쉬웠던 부분으로 MySQL과 MongoDB간의 차이점을 RDB와 NoSQL간 차이점 외에 설명하지 못했다는것이었다

## 60. [기술면접] Spring 면접질문 (2)

- URL: https://velog.io/@rdamin/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-Spring-%EB%A9%B4%EC%A0%91%EC%A7%88%EB%AC%B8-2
- Source: velog
- Roles: ['unknown']
- Published: 2024-12-31
- Freshness: recent
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - DI가 뭔지 객체지향관점을 연결지어 말하기
  - JWT(Json Web Token)에 대해 간단히 설명
  - OAuth에 대해 간단히 설명해주세요
  - JWT와 OAuth의 차이는 무엇이 있을까요?
  - 저희 프로젝트에서는 프론트엔드(Vue.js) 와 백엔드(Spring Boot) 가 서로 다른 도메인에서 동작하고 있었고, 예를 들어 프론트엔드는 http://localhost:5173 , 백엔드는 http://localhost:8080에서 실행되었습니다

## 61. 📒 기술면접 정리 ( Spring )

- URL: https://velog.io/@rlaghwns1995/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A0%95%EB%A6%AC-Spring
- Source: velog
- Roles: ['unknown']
- Published: 2021-10-12
- Freshness: old
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 스프링 프레임워크란 ?
  - MVC 구조란 ?
  - DispatcherServlet이란 ?
  - 반대로 말하면 스프링에게 애플리케이션의 흐름을 제어하는 권한(IoC)이 없다면?

## 62. [후기]제로베이스 백엔드 스쿨 9기를 끝내며(400만원 돈값 하나?)

- URL: https://velog.io/@wsh096/%ED%9B%84%EA%B8%B0%EC%A0%9C%EB%A1%9C%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%8A%A4%EC%BF%A8-9%EA%B8%B0-%EC%A2%85%EA%B0%95-%ED%9B%84%EA%B8%B0%EB%82%B4-%EC%B9%B4%EB%93%9C%EA%B0%92%EC%9D%80-%EC%97%AC%EC%A0%84%ED%9E%88-%EC%88%98%EA%B0%95-%EC%A4%91
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2023-07-02
- Freshness: recent
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - [후기]제로베이스 백엔드 스쿨 9기를 끝내며(400만원 돈값 하나?
  - [후기]제로베이스 백엔드 스쿨 9기를 끝내며(400만원 돈값 하나?
  - 가치 단점 백엔드스쿨 부트캠프 수강후기 장단점 장점 제로베이스 종강
  - 알고리즘에 대해서는 어떻게 생각하시는지?
  - 전공한 분들과 놓고 대화해도 Java 문법을 활용하고 코딩하는데는 문제가 없다고 생각할 수준으로 3개월의 노력으로 도달할 수 있는 방법은 제가 경험한 바로는 이 밖에는 없었습니다

## 63. (항해99) 신입 Back-End 개발자 취업 후기

- URL: https://velog.io/@point/%ED%95%AD%ED%95%B499-%EC%8B%A0%EC%9E%85-Back-End-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EC%97%85-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'frontend']
- Published: 2022-03-17
- Freshness: old
- Rule score: 47
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - spring이 아니라 node.js를 선택한 이유 (학부 때 했던 java가 익숙할 텐데 왜 java 하다가 javascript하는지

## 64. 보이지 않는 곳에서 실전 AI의 기반을 만드는 백엔드팀 | MakinaRocks

- URL: https://www.makinarocks.ai/blog/%EB%A7%88%ED%82%A4%EB%82%98%EB%9D%BD%EC%8A%A4-%EB%B0%B1%EC%97%94%EB%93%9C%ED%8C%80-%EC%9D%B8%ED%84%B0%EB%B7%B0/
- Source: www.makinarocks.ai
- Roles: ['ai_ml_data', 'devops_infra', 'backend', 'cs_common', 'frontend']
- Published: 2025-12-05
- Freshness: recent
- Rule score: 46
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 년 이상 여러 도메인의 시스템을 개발하면서 다양한 문제를 접해 왔는데, 특히 머신러닝·데이터 기반 문제 해결에 흥미가 많았습니다
  - 백엔드팀의 역할은 회사 성장과 함께 어떻게 확장되었나요?
  - 백엔드 개발자로서 기술적 경험의 폭을 넓힐 수 있는 포지션이라고 생각합니다
  - 백엔드팀에서 일하면서 가장 크게 성장했다고 느낀 순간은 언제였나요?
  - 그렇다면 백엔드 포지션은 어떤 분과 잘 맞을까요?

## 65. 2023 상반기 팀네이버 공채 합격 후기 (feat. 백엔드)

- URL: https://ppaksang.tistory.com/31
- Source: tistory
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2023-07-20T00:16:40+09:00
- Freshness: recent
- Rule score: 45
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 이때, 여러 빅테크 기업에서 운영하는 기술 블로그, 유튜브에서 현업에서는 기술을 어떻게 사용한지 정리하고 학습했다

## 66. 💡 [@@소프트 면접 후기] 신입 개발자 면접 경험 공유 (기술 면접 질문 포함)

- URL: https://velog.io/@hyun70022/%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'frontend', 'ai_ml_data']
- Published: 2025-01-29
- Freshness: recent
- Rule score: 45
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - "JavaScript에서 비동기 처리(Ajax, Promise, async/await)의 장점은?"

## 67. 게임 클라이언트 개발자 면접질문 정리

- URL: https://velog.io/@audwns356/%EA%B2%8C%EC%9E%84-%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'cs_common', 'devops_infra', 'frontend']
- Published: 2023-11-30
- Freshness: recent
- Rule score: 45
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 이를 해결하기 위해 여러 도구와 기술을 활용하고, 코드 리팩토링과 효율적인 알고리즘 적용을 위해 노력했습니다
  - 게임 클라이언트 분야에서 가장 최근에 관심을 가지거나 학습한 것이 무엇인가요?
  - 자료구조가 뭔가요?
  - Dictionary내부 동작 원리

## 68. 2025 네이버 신입 공채 최종 합격 후기: Tech 백엔드 (KOR)

- URL: https://skykhs3.github.io/posts/team-naver-recruitment-review/
- Source: skykhs3.github.io
- Roles: ['backend', 'ai_ml_data', 'frontend', 'cs_common', 'devops_infra']
- Published: 2025-07-03T16:13:00+09:00
- Freshness: recent
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 알고리즘 강점은 저의 문제해결 능력을 보여주기 위한 것이고, 백엔드 개발자 근무 경험은 현업 적응력을 보여주기 위한 것입니다
  - 📱 포인트만 쏙쏙 📚 이것이 우분투 리눅스다 - 백엔드 개발자라면 능숙한 리눅스 사용은 필수 📚 클린 코드 - 가독성이 좋은 코드란 무엇인가 📚 리팩터링 2판
  - 도커/쿠버네티스 - 쿠버네티스 경험은 백엔드 신입 개발자 한테도 요구하는 사항이라고 생각합니다

## 69. [멋사] 멋쟁이사자처럼 대학 11기 면접 최종 합격 후기(+2번이나 떨어진 줄 알았던 썰..)

- URL: https://codingtoday.tistory.com/19
- Source: tistory
- Roles: ['backend', 'frontend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2023-03-26T00:13:32+09:00
- Freshness: recent
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 같은 분야(백엔드)면 그런 식으로 가능한데, 다른 분야(프론트엔드, 디자인)에서 갈등이 생기면 어떻게 해결할 것이냐?
  - 년동안 java를 써왔으면 선호하는 프레임워크가 있을 텐데, 어떤 걸 선호하나?
  - 파이썬과 장고 중에 선호하는 언어가 있는지?
  - 자바 vs 파이썬이면 이해하겠는데 파이썬 vs 장고..?
  - 면접 끝나고는 "혹시 내가 스프링, 장고라는 프레임 워크를 알고 있는지 떠보신 건가..?"라는 생각도 했다

## 70. 2023 ICT 상반기 인턴십 면접 후기

- URL: https://sons6488.tistory.com/3
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra', 'ai_ml_data']
- Published: 2023-02-18T21:57:59+09:00
- Freshness: recent
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드 직무 희망했으면 다른 서비스의 백엔드를 분석해본 경험이 있는지
  - 그래도 백엔드 분석해본 경험 질문은 좋았던거 같다
  - 휠세이프(프로젝트 명) 에 대해서 설명해주세요(알고리즘 설명 및 갈등 해소 경험
  - 백엔드 API 및 CI/CD 데이터파이프라인 구축 직무였는데 OS와 메모리효율 등 CS적인 기초 지식을 중요시하는거 같았다 왜냐면 개발을 하다보면 기초 지식들이 알게 모르게 다 녹아들어간다고 그랬다

## 71. 부트캠프 수료 후 1년만에 개발자 취업 후기 및 2024 회고

- URL: https://velog.io/@ystar5008/%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%88%98%EB%A3%8C-%ED%9B%84-1%EB%85%84%EB%A7%8C%EC%97%90-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EC%97%85-%ED%9B%84%EA%B8%B0-%EB%B0%8F-2024-%ED%9A%8C%EA%B3%A0
- Source: velog
- Roles: ['unknown']
- Published: 2025-01-03
- Freshness: recent
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - "프로젝트에서 JWT 토큰을 사용하셨는데 그 이유가 뭔가요?" 라는 질문이 날아왔다
  - "자바스크립트에서 배열과 객체의 차이가 무엇인가요?"
  - 면접 질문 정리: https://lively-quokka-d71.notion.site/153480a3853d80a4bd25ed412b516d7f?pvs=

## 72. 🎞️휴맥스 드림버스컴퍼니 지원&면접 후기

- URL: https://velog.io/@dlgkdis801/%ED%9C%B4%EB%A7%A5%EC%8A%A4-%EB%93%9C%EB%A6%BC%EB%B2%84%EC%8A%A4%EC%BB%B4%ED%8D%BC%EB%8B%88-%EC%A7%80%EC%9B%90%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-10-19
- Freshness: recent
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - OO 서버는 어떤 로직으로 구성했나요?
  - OO 클래스와 OO 알고리즘은 어떻게 이용했나요?
  - Spring, SpringBoot, SpringSecurity에 대해서 설명해보세요
  - Redis는 어떤 DB인지 설명해주실래요?
  - Github, Postman, AWS는 어느 정도로 사용이 가능하신가요?

## 73. [CJ올리브영] 백엔드 1차 직무면접 후기

- URL: https://jie0025.tistory.com/523
- Source: tistory
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2023-05-09T15:15:11+09:00
- Freshness: recent
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - AI 원리 학습

## 74. 인턴 후기 | 24년 겨울, CUop 래블업 백엔드 개발자 인턴 후기 -서류/면접 편-

- URL: https://dev-mintcat.tistory.com/9
- Source: tistory
- Roles: ['ai_ml_data', 'backend', 'cs_common', 'devops_infra']
- Published: 2025-04-28T16:47:38+09:00
- Freshness: recent
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 이때 container 기술 중 하나인 Docker 사용을 제시해서 해결함
  - Git과 GitHub 사용 능력은 필수인데, 사용 경험이 있는지?
  - Docker 사용 경험은 있는지?

## 75. [당근마켓 윈터테크] 2021 하반기 당근마켓 윈터테크 인턴십 서류 합격, 면접 후기 (백엔드 개발)

- URL: https://0m1n.tistory.com/2
- Source: tistory
- Roles: ['backend', 'frontend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2021-12-25T11:30:28+09:00
- Freshness: old
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 스프링 핵심 원리,

## 76. NHN 엔터프라이즈 개발자 면접 후기 - T인터뷰편

- URL: https://cookie-dev.tistory.com/15
- Source: tistory
- Roles: ['backend', 'devops_infra', 'cs_common']
- Published: 2023-06-02T01:45:06+09:00
- Freshness: recent
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 성공과 실패를 결정하는 1%의 네트워크 원리

## 77. 신입 개발자 기술면접 질문 리스트

- URL: https://velog.io/@harry__/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8
- Source: velog
- Roles: ['unknown']
- Published: 2023-12-14
- Freshness: recent
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 💡 Java의 특징을 설명해주세요
  - JVM(자바가상머신) 위에서 동작하기 때문에 운영체제가 독립적이다
  - JVM은 스택 기반으로 동작하며, Java Byte Code를 OS에 맞게 해석 해주는 역할을 하고 가비지컬렉션을 통해 자동적인 메모리 관리를 해준다
  - 💡 Java의 컴파일 과정에 대해 설명해주세요
  - 💡 Java에서 제공하는 원시 타입들에 무엇이 있고, 각각 몇 바이트를 차지하나요?

## 78. 20220103 면접후기

- URL: https://velog.io/@jihye/20220103-%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-01-03
- Freshness: old
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 프로젝트에서 어떤 기능을 맡아서 개발하였는지, 사용한 라이브러리는 어떤 것이 있는지같이 예상 가능한 질문들도 있었고, 지난번 모의 면접때처럼 http와 https의 차이는 무엇인지 아는지 물어보셨다
  - 여러 분야중 왜 백엔드를 선택했는지에 대한 질문도 하셨다
  - JAVA란 무엇일까?

## 79. [회고] 2024 SSAFY 공통 프로젝트 - "Speechless" 회고

- URL: https://velog.io/@cloud_365/%ED%9A%8C%EA%B3%A0-2024%EB%85%84-SSAFY-%EA%B3%B5%ED%86%B5-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0
- Source: velog
- Roles: ['unknown']
- Published: 2024-02-18
- Freshness: recent
- Rule score: 42
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Transaction 문제는 해결했으나 openVidu 서버로 요청을 보내는 과정에서 위 에러가 발생했다
  - 결국 openVidu 포트로 접속해 이미 등록된 인증서를 가져와 keytools를 가지고 JAVA에 인증서를 추가하고 문제가 해결됐다

## 80. 2차 면접 후기 정리

- URL: https://velog.io/@god0478/2%EC%B0%A8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0-%EC%A0%95%EB%A6%AC
- Source: velog
- Roles: ['unknown']
- Published: 2024-10-25
- Freshness: recent
- Rule score: 42
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 기술면접에서 물어보셨던게 일단 프로젝트 관련해서 jwt header 말로 다른 방법으로 보낼 수있는 방법이 있을까요?
  - 하 전에 배웠던 개념이긴한데 조금 오래되서 의존개념이 내가 직접 주입하냐 스프링이 주입하냐에 차이인데 간단하게 내가 주입하게 될 경우 라이플 사이클이냐 객체 생성을 직접해야 되기때문에 코드가 길어질 수 있고 이걸 스프링이 해주게되면 코드도 줄어들고 라이프사이클을 알아서 관리해준다

## 81. 면접 후기

- URL: https://velog.io/@the100-00/%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'frontend', 'ai_ml_data']
- Published: 2022-07-21
- Freshness: old
- Rule score: 42
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 데이터베이스 관련 경험이 있다면 말해보라
  - 다양한 프로젝트 경험으로 오라클, mysql, sqlite 사용 경험이 있다고 답함
  - 만약 입사 후 프론트엔드 개발이나 배치 등 원하던 업무가 아닌 업무를 맡게 된다면?
  - 트랜잭션 어노테이션 사용 경험 있는지?
  - 스프링 시큐리티 사용 경험이 있는지?

## 82. 2024 미래내일 일경험 IT 백엔드 개발자 면접 후기

- URL: https://eod940.tistory.com/55
- Source: tistory
- Roles: ['unknown']
- Published: 2024-05-18T22:04:31+09:00
- Freshness: recent
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 미래내일 일경험 IT 백엔드 개발자 면접 후기
  - 미래내일 일경험 IT 백엔드 개발자 면접 후기
  - 파이썬과 자바 언어의 차이
  - 스프링 시큐리티 설명 부탁드립니다
  - 스프링 컨테이너에 대해서 설명해주세요

## 83. [UMC 8기] Spring Boot 파트 서류&면접 합격 후기

- URL: https://velog.io/@jayaione_ele/UMC-8%EA%B8%B0-Spring-%ED%8C%8C%ED%8A%B8-%EC%84%9C%EB%A5%98%EB%A9%B4%EC%A0%91-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2025-03-20
- Freshness: recent
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 스프링과 스프링부트의 차이
  - Node.js와 Spring 경험이 둘 다 있는데, 둘의 장단점 및 차이점
  - 서버 요청이 많을 때 해결 방법
  - API, REST API에 대한 설명
  - Oauth와 자체 로그인의 차이

## 84. 2025 상반기 ICT 학점연계 인턴십 지원 후기 (최종 합격)

- URL: https://velog.io/@dzcoffee/2025-%EC%83%81%EB%B0%98%EA%B8%B0-ICT-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EC%A7%80%EC%9B%90-%ED%9B%84%EA%B8%B0-%EC%B5%9C%EC%A2%85-%ED%95%A9%EA%B2%A9
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2025-04-06
- Freshness: recent
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 현재 기업이 직면한 여러 기술적인 문제, CDN과 AWS Cloud 설계들을 배우고 Spring Boot에서 기존에 사용하지 않았던 기술과 문제들을 새롭게 파악하고 해결해 나아가고 있습니다

## 85. SOPT 28기 웹파트 면접 후기

- URL: https://velog.io/@hojin11choi/SOPT-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'frontend', 'cs_common', 'ai_ml_data']
- Published: 2021-03-24
- Freshness: old
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - github, 블로그가 있다면 주소 + 지금까지의 프로그래밍 경험
  - 난 분명 지원서에 백엔드 경험이 풍부하고 리액트는 정말 기본 개념 강의만 들었다고 했는데 class component vs function component 물어보셔서 너무 당황했다
  - 다른 SOPT 면접 후기들을 보니 JavaScript let, var, const 차이 이런거 물어보시던데!...!!
  - 했는데 생각해보니 내가 서버 파트로서의 경험이 있기 때문에 그거에 맞춘 질문을 더 많이 하신것 같았다
  - 만약 나만큼의 경험이 없는 사람이라면, (HTML, CSS, JS 언어 공부해본 정도라면) 아래의 질문들 정도를 물어보시지 않을까 싶다

## 86. 신입 개발자 면접 질문

- URL: https://www.catchmiru.com/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8/
- Source: www.catchmiru.com
- Roles: ['frontend', 'backend', 'cs_common', 'ai_ml_data']
- Published: 2025-04-05T16:19:59+09:00
- Freshness: recent
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 개인 프로젝트와 교내 해커톤에서 주로 JavaScript를 사용하여 프론트엔드를 구현했고, Node.js를 활용한 백엔드 개발도 경험해봤습니다
  - ➡ 팁 : 간단한 코드 구현 경험이나 GitHub 포트폴리오 링크를 함께 언급하면 신뢰도가 올라갑니다
  - 비전공자라도 자신만의 학습 방법, 프로젝트 경험, 꾸준한 열정을 보여준다면 충분히 경쟁력이 있습니다

## 87. 백엔드 중소기업 첫번째 면접 후기

- URL: https://velog.io/@robolab1902/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85-%EC%B2%AB%EB%B2%88%EC%A7%B8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-01-19
- Freshness: old
- Rule score: 40
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 기억 나는 것만 살짝 생각해보면, Framework 중 MVC 모델이 무엇이고 MVC 모델을 쓰는 종류엔 무엇이 있냐
  - AOP와 DI를 설명해보아라
  - JPA의 영속성 컨텍스트가 해주는 역할이 무엇이냐?
  - [Spring] DI가 무엇일까?

## 88. [2024.10 ~ 2024.12] 백엔드 개발 3개월 인턴 회고 (+ 면접 후기)

- URL: https://wooing1084.tistory.com/42
- Source: tistory
- Roles: ['unknown']
- Published: 2025-03-17T15:42:58+09:00
- Freshness: recent
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Git의 통신은 어떻게 동작할까?
  - Git의 통신은 어떻게 동작할까?
  - JPA에 대한 설명

## 89. UMC 5기 합격 후기 (서버 Spring 파트, 울산대학교)

- URL: https://raon-2.tistory.com/33
- Source: tistory
- Roles: ['unknown']
- Published: 2023-09-12T09:37:53+09:00
- Freshness: recent
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 면접 질문 으로는 왜 서버에 지원했는지, JPA, JDBC,MVC 패턴, rest api와 api의 차이 등 에 대해서 여쭤보셨어요
  - 제가 지난 4기 UMC에 웹이었고, 서버에 대한 경험이 없어서 그런지 그에 맞춰서 면접 질문을 내주신 것 같았어요.(개인적인 생각입니다 실제로 그러신게 아님
  - [Github/Git] 깃허브 PR이란?

## 90. JavaScript 신입 백엔드 개발자 기술 면접 후기

- URL: https://velog.io/@s_hajin/JavaScript-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-05-12
- Freshness: recent
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 웹 브라우저에서의 JS와 Node.js의 차이점
  - DB 설계는 어떻게 했는지
  - DB 쿼리문을 작성하기 위해 연결을 어떻게 했는지

## 91. [스타트업 백엔드 일기😕] 경력직 이직 개발자 질문 리스트 정리

- URL: https://velog.io/@jee-9/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%97%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%9D%BC%EA%B8%B0-%EA%B2%BD%EB%A0%A5%EC%A7%81-%EC%9D%B4%EC%A7%81-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%A7%88%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A6%AC
- Source: velog
- Roles: ['unknown']
- Published: 2025-03-05
- Freshness: recent
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Django와 mysql을 함께 사용한 이유는 무엇인가 (Django의 권장사항은 PostgresQL이라고 합니다
  - https와 http의 차이 (아 이건 공개키 이야기를 했어야하는데...단어가 ㅠ
  - 경험을 말하며) 이렇게 대답했고, b-tree 관련해서는 ElasticSearch LIKE 쿼리에서 본 내용들을 토대로, 이런 개념인 것을 이해한다

## 92. 미래내일 일경험 인턴형 3곳 전부 합격 면접 및 인턴 후기

- URL: https://velog.io/@dandonedan/%EB%AF%B8%EB%9E%98%EB%82%B4%EC%9D%BC-%EC%9D%BC%EA%B2%BD%ED%97%98-%EC%9D%B8%ED%84%B4%ED%98%95-3%EA%B3%B3-%EC%A0%84%EB%B6%80-%ED%95%A9%EA%B2%A9-%EB%A9%B4%EC%A0%91-%EB%B0%8F-%EC%9D%B8%ED%84%B4-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'frontend', 'cs_common']
- Published: 2025-09-23
- Freshness: recent
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 스킬 및 역량에서 컴퓨터 비전 이해도가 70퍼센트고 딥러닝 이해도가 60퍼센트인데 이정도면 상당히 높은 수치인데 어떤걸 기준으로 책정했나요?
  - Vue.js : 해당 이전에는 html, js, css를 가지고 단순하게 프론트엔드 에러 해결 및 개선 경험이 있는데 러닝커브가 짧다는 소식에 공부와 동시에 개발을 병행하였다
  - Django, Flask, FastAPi 중 Flask로는 웹서비스 개발 경험이 있었지만 FastAPI가 속도나 결합성 등 여러 측면에서 더 우수하다고 생각되어 해당 기술을 선정했다

## 93. 간단한 면접 후기

- URL: https://velog.io/@god0478/%EA%B0%84%EB%8B%A8%ED%95%9C-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2024-10-16
- Freshness: recent
- Rule score: 38
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - redis, elasticCache?
  - 자바스크립트 es6 이란 무엇인가 ?
  - jwt vs session 차이
  - es6 이게 뭔말인지 몰랐던게 자바스크립트 표준 버전이였다 간단하게 const let var 이런거가 어떤 식으로 사용되고 어떻게 활용되는지 에대한 표준 이런거 였는데 이것을 통틀어서 저렇게 말하는지 솔직히 처음알았다

## 94. 2026 카카오 그룹 신입 크루 공채 후기 (2) - 1차 면접, 2차 면접, 최종 합격

- URL: https://velog.io/@heiler/2026-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B7%B8%EB%A3%B9-%EC%8B%A0%EC%9E%85-%ED%81%AC%EB%A3%A8-%EA%B3%B5%EC%B1%84-%ED%9B%84%EA%B8%B0-2-1%EC%B0%A8-%EB%A9%B4%EC%A0%91-2%EC%B0%A8-%EB%A9%B4%EC%A0%91-%EC%B5%9C%EC%A2%85-%ED%95%A9%EA%B2%A9
- Source: velog
- Roles: ['cs_common', 'backend', 'ai_ml_data', 'devops_infra']
- Published: 2026-03-23
- Freshness: recent
- Rule score: 38
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 대신 여러 분야(보안, 알고리즘, ML/DL, 백엔드 부트캠프)의 경험 + 탄탄한 CS 베이스 지식을 갖고 있다는 것을 어필했습니다
  - ACM-ICPC 본선 경험, 보안학과 졸업, 대학원 진학(로봇 + 강화학습 연구실), 대학원 자퇴 후 군대, 수학학원 선생님, 웹 개발 부트캠프(우아한테크코스) 수료, 백엔드 개발자 취업 준비
  - 서류에 적은 경험 중에 로그 모니터링 시스템 구축 경험이 있었는데 관련해서 조금 깊게 질문을 받았습니다
  - 제가 비록 백엔드 개발자로써 학습을 시작한 기간은 짧았으나, 성장 가능성을 더 알아봐주셨다고 밖에 설명할 수 없을 것 같습니다

## 95. 자바, 스프링, 실무 경험? 모두 다 잡아보는 백엔드 개발자 부트캠프 추천 - 내일배움캠프 블로그

- URL: https://nbcamp.spartaclub.kr/blog/%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%B6%94%EC%B2%9C-23918
- Source: nbcamp.spartaclub.kr
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2024-07-12T06:13:00+00:00
- Freshness: recent
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 자바, 스프링, 실무 경험?
  - 자바, 스프링, 실무 경험?
  - 왜 Java, Spring일까?
  - 빈약한 포트폴리오, 적은 프로젝트 경험에 걱정하고 계시다면, 백엔드 개발자에 초점을 맞춘 내일배움캠프 백엔드 트랙을 추천드립니다
  - 왜 Java, Spring일까?

## 96. 두나무 수시채용 합격 후기

- URL: https://unluckyjung.github.io/recruit_story/2022/03/22/Dunamu/
- Source: unluckyjung.github.io
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'frontend']
- Published: 2022-03-22T15:00:00+09:00
- Freshness: old
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 면접은 편안한 분위기에서 진행되었고, 면접 극초반부에 살짝 네트워크 이슈가 있었지만 해결 과정속에서 CTO님과 이런저런 이야기를 하며 자연스럽게 아이스브레이킹이 되었고, 오히려 이 덕분에 면접을 잘 진행 할 수 있었다고 생각합니다

## 97. 비전공자의 백엔드개발자 면접후기

- URL: https://velog.io/@9ruem2/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90%EC%9D%98-%EB%B0%B1%EC%97%94%EB%93%9C%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-12-19
- Freshness: recent
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - api문서화를 하면서 목객체를 사용할 수 있는데 왜 swagger를 사용했나?
  - http메서드에 대해 설명해보라
  - 시큐리티는 api문서화할 때 어떻게 적용했나?
  - mvc패턴은 어떤것을 사용했나?
  - 데이터베이스는 어디수준까지 알고있나?

## 98. 면접 질문 정리 및 후기

- URL: https://velog.io/@god0478/%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC-%EB%B0%8F-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2025-03-11
- Freshness: recent
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 늘있는 n+1 문제 db구조와 엔티티 구조가 다르기 때문에 발생하는 문제 보통 fetch join이나 batsize를 사용해서 한번에 데이터를 긁어와서 해결
  - redis 관련해서 분산락에 대한 질문 reddisson 방식과 lettuce 방식의 차이점
  - 그리고 인증 관련해서 jwt 방식과 session 방식의 차이 그리고 jpa와 hibernate가 뭐고 어떤 차이가있는지 에대한 질문이였습니다
  - 그리고 객체지향을 무엇이고 왜 쓰는지 에대한 질문 등등 엄청 많았는데 여기에 뭐 알고리즘에 대한 이야기등 솔직히 기술 면접이라고 해가지고 뭐 간단한거나 코태 볼줄 알았는데 정의나 개념 관련해서 너무 자세하게 물어보셔서 당황했습니다

## 99. 당근마켓 면접 후기 및 회고

- URL: https://velog.io/@dion/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0-%EB%B0%8F-%ED%9A%8C%EA%B3%A0
- Source: velog
- Roles: ['unknown']
- Published: 2020-11-07
- Freshness: old
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 당근마켓에서는 알고리즘 문제 말고 실제 문제를 해결할 역량을 갖춘 개발자를 원하는 느낌 을 받았습니다
  - 백기선님 온라인 스터디 1주차 - JVM은 무엇이며 자바 코드는 어떻게 실행하는 것인가
  - velog 메인에서 보고 궁금해서 들어왔는데 Dion 글이었군요 ㅎㅎ 좋은 경험 공유해주셔서 감사합니다

## 100. [SSU] 현직자 세미나_카카오뱅크 백엔드

- URL: https://velog.io/@riinnn/SSU-%ED%98%84%EC%A7%81%EC%9E%90-%EC%84%B8%EB%AF%B8%EB%82%98%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%B1%85%ED%81%AC-%EB%B0%B1%EC%97%94%EB%93%9C
- Source: velog
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2023-09-23
- Freshness: recent
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 초반에 알고리즘 관련 내용이 길어서(어떻게 풀어야하는지 보다는 기타 부수적 이야기..?) 루즈해지는 감이 조금 있었지만 그 부분을 제외한 나머지는 전반적으로 유익했다
  - 지난 프로젝트에서 '스프링부트' 를 사용하여 ~한 경험을 했다
  - => 지난 프로젝트에서 'SpringBoot' 를 사용하여 ~한 경험을 했다
  - 따라서, 알고리즘의 경우 코테를 통과했으면 된 것이기 때문에 이에 관련된 내용보다는 프로젝트 위주로 설명하는 것이 좋다고 하셨다
  - 그에따라 면접관에게 다소 생소할 수 있는 알고리즘과 관련된 내용보다는 프로젝트에서 본인이 기여한바, 어떤 경험을 했는지와 관련된 요소를 어필하는 것이 더 좋다고 하셨다

## 101. 2025 가비아 신입 백엔드개발자 자기소개서와 면접자료 대학레포트 자기소개서

- URL: https://www.reportshop.co.kr/rpts/2643276
- Source: www.reportshop.co.kr
- Roles: ['backend', 'ai_ml_data', 'cs_common']
- Published: 2025-09-04
- Freshness: recent
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 네이버와 같은 대규모 트래픽을 처리하는 서비스에서는 단순한 기능 구현을 넘어, 확장성, 안정성, 성능 최적화가 중요한 요소이며, 저는 이를 해결하는 백엔드 개발 분야에 매력을
  - 백엔드 테스트 케이스 작성을 자발적으로 맡아 기여했고, 그 덕분에 빠르게 중심 멤버로 성장할 수 있었습니다.보안에 대해 어떻게 준비해왔나요?
  - 대학 시절 처음 웹 프로젝트를 진행하며 사용자가 증가할수록 서버가 불안정해지는 경험을 한 적이 있습니다
  - 이 경험을 통해 눈에 보이지 않는 영역을 설계하고 최적화하는 백엔드의 가치와 즐거움을 깨달았습니다
  - 저는 학부와 인턴 경험을 통해 보안 프로그래밍 기법과 DB 최적화를 학습하며 이러한 역량을 키웠습니다

## 102. 하반기 삼성전자 DX SW개발 지원 후기

- URL: https://sirong-blog.tistory.com/entry/%ED%95%98%EB%B0%98%EA%B8%B0-%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-DX-SW%EA%B0%9C%EB%B0%9C-%EC%A7%80%EC%9B%90-%ED%9B%84%EA%B8%B0
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra', 'frontend']
- Published: 2023-12-09T20:03:25+09:00
- Freshness: recent
- Rule score: 36
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 잘은 모르지만, dx 알고리즘 특강을 듣고 dx를 지원해서인걸까..?
  - 리액트는 무슨 웹서버를 이용해서 호스팅 될까?

## 103. 2025 네이버 신입 공채 Tech 최종 합격 회고 (Backend)

- URL: https://velog.io/@kyumericano/2025-naver-retrospect
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'cs_common']
- Published: 2025-06-24
- Freshness: recent
- Rule score: 36
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 총 4번의 멘토 경험, 안드로이드 앱 개발, 풀스택 앱 개발, MSA 설계 등을 교육
  - 실제로 저는 MSA에 매우 관심이 많았고, 창업을 포함한 다양한 프로젝트에서 MSA를 적용을 하는 경험을 했습니다
  - CQRS 를 직접 구현을 한다거나, 메세지 큐를 활용하여 EDA 를 설계하여 비동기 처리를 하는 등등, MSA를 공부하는 것에 그치지 않고, 실제로 그 아키텍쳐를 설계하며 구현을 하는 경험 을 하였습니다
  - 이 과정에서 Token Bucket 알고리즘을 차용한 Rate Limit 기능을 개발하고, 더 나아가 서버 다중화 + Load Balancing 을 적용하여 대용량 트래픽을 처리했다는 경험을 강조하였습니다
  - Chat GPT 는 생각 이상으로 면접 질문을 잘 만들어주고, 아니 이런 질문을 한다고?

## 104. 프론트엔드 개발자 인터뷰 후기 (면접 질문 정리)

- URL: https://velog.io/@tmmoond8/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B8%ED%84%B0%EB%B7%B0-%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC-%EC%9E%91%EC%84%B1-%EC%A4%91
- Source: velog
- Roles: ['unknown']
- Published: 2018-11-16
- Freshness: old
- Rule score: 35
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 클라이언트 쪽의 스크립트(예: 자바 스크립트)를 다루는 방식에 차이가 있다
  - '인사이드 자바스크립트' 책과 등 실행컨텍스트를 설명하는 많은 곳에서 기준이 되는 버전은 es3 버전이라고 합니다
  - zerocho님의 Node.js 교과서에 참고 자료로 이벤트 루프에 대한 시각적 설명 링크가 있는데, 이벤트 루프를 이해하기 좋을 것 같습니다
  - < script type = " text/javascript " src = " http://kingbbode.com/result.json?callback=parseResponse " > </ script >

## 105. 면접 회고 01

- URL: https://velog.io/@kimlh2/%EB%A9%B4%EC%A0%91-%ED%9A%8C%EA%B3%A0-01-h0dh6lhd
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2022-04-14
- Freshness: old
- Rule score: 35
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 과제에서 개선할 점은 없는지 캐시를 사용한 의도가 무엇인지 등등을 물어보셨다

## 106. 현대오토에버 24년 10월 신입채용 1차면접 후기 (백엔드/차량 관제)

- URL: https://xorjsghkd1011.tistory.com/173
- Source: tistory
- Roles: ['unknown']
- Published: 2024-12-04T11:41:54+09:00
- Freshness: recent
- Rule score: 33
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 새 프로젝트에서 MongoDB, Redis 사용 예정 → 둘다 NoSQL인데 차이는?
  - CI/CD 파이프라인 구축 경험 → 거기서 git도 사용해봤는지?
  - git이 파이프라인에서 어떻게 활용되는가?

## 107. [최종 불합] 2025 팀네이버 신입 공채:Tech (백엔드) 후기

- URL: https://velog.io/@yusungkk/%EC%B5%9C%EC%A2%85-%EB%B6%88%ED%95%A9-2025-%ED%8C%80%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%8B%A0%EC%9E%85-%EA%B3%B5%EC%B1%84Tech-%EB%B0%B1%EC%97%94%EB%93%9C-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'ai_ml_data']
- Published: 2025-07-04
- Freshness: recent
- Rule score: 33
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 졸업 후, 백엔드 부트캠프를 6개월간 들으면서 한 프로젝트 경험이 전부(유명한 부트캠프X
  - 차근차근 메서드 익히고, 다양한 알고리즘 익히고, 다른 분들 풀이 보면서 어떻게 접근하면 좋을지 탐구했습니다
  - 그래서 그냥 평소에 준비하던대로 포트폴리오 기반 내용 정리, 알고리즘/CS 내용 정리 등을 함과 동시에 인성 질문 리스트들을 보면서 이런 질문이 오면 어떻게 답변하면 좋을까 한번 생각해보고 의도가 뭔지 찾아 보고 이렇게 준비했던 것 같습니다

## 108. 조개전골챗(?) 후기

- URL: https://velog.io/@ddoddiworld/%EC%A1%B0%EA%B0%9C%EC%A0%84%EA%B3%A8%EC%B1%97-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'frontend']
- Published: 2024-02-01
- Freshness: recent
- Rule score: 33
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 면접 경험에서 2번씩이나 백엔드를 몰라서 컷 당했다는 말씀을 드렸더니 이해할 수 없다고 하셨다
  - 프론트엔드한테 백엔드를 물어보는게 좀 이상하긴 하지만 국내에선 큰 회사가 아니면 대부분 프론트-백엔드를 모두 경험하기 때문에 그런 질문을 하셨던게 아닐까?라고 말씀해주셨다
  - 왜냐하면 프론트엔드는 보통 노드 모듈을 기반으로 개발을 하는데 이 노드 모듈을 잘 다루는 사람이 그렇게 많지 않다고 한다

## 109. [백엔드 개발 채용 프로세스] IT기업의 1차 면접과 2차 면접

- URL: https://www.hanbit.co.kr/channel/view.html?cmscode=CMS9969478288
- Source: www.hanbit.co.kr
- Roles: ['backend', 'cs_common', 'ai_ml_data']
- Published: 2024-01-19
- Freshness: recent
- Rule score: 32
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 여러분이 학습한 CS  지식을 개발 과정에 접목해 보고, 반대로 개발하면서 경험했던 내용 또한 CS 지식을 학습하면서 떠 올려 보셔야 합니다
  - 의외로 많은 지원자가 잘 답변하지 못하는 내용은 ‘왜 ◯◯ 언어로 개발했는가?’, ‘왜 ◯◯ 데이터베이스를 사용했는가?’ 등과 같은 기초적인 질문입니다
  - [백엔드 개발이란?] 웹 개발 분야의 프런트엔드와 백엔드

## 110. IT 산업기능요원 보충역(신입 프론트엔드 개발자) 구직 후기

- URL: https://velog.io/@jybesiu/IT-%EC%82%B0%EC%97%85%EA%B8%B0%EB%8A%A5%EC%9A%94%EC%9B%90-%EB%B3%B4%EC%B6%A9%EC%97%AD-%EA%B5%AC%EC%A7%81-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['frontend', 'backend', 'cs_common', 'ai_ml_data']
- Published: 2021-09-25
- Freshness: old
- Rule score: 31
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 캠프를 하면서 프론트, 백을 둘 다 어느 정도 경험해 본 상태에서 프론트가 더 잘 맞을 것 같아 프론트엔드 개발자 로 포지션을 정했다

## 111. 신입 개발자의 한중일 취준 회고

- URL: https://velog.io/@railgunofpku/igotajob
- Source: velog
- Roles: ['frontend', 'ai_ml_data', 'backend', 'cs_common']
- Published: 2024-12-04
- Freshness: recent
- Rule score: 31
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 진부하지만, 누구나 알고 있는 좋은 학교에 다니고 있다는점, 또한 이 학교를 다니며 개발자에게 중요한 빠른 학습 능력을 가지고 있으며, 이를 증명할 수 있는 경험/사례가 있다는 점
  - 예를 들어, 위에 보이는것 처럼 제가 리액트의 기초 내부 작동 원리에 대해 자신이 있다고 써놓은걸 보시고, 이 한 문장때문에 제 면접에 리액트 내부 동작 이해도를 확인할 수 있을지 시험하는 코드를 2가지나 작성해오신 면접관님이 계신 경우가 있었습니다
  - CS관련 질문을 하는 회사 한정) 다른건 몰라도 OS, 네트워크의 기초적인 부분들만큼은 제대로 이해하고 있는지?

## 112. 백엔드 개발자 신입 스타트업 면접후기

- URL: https://sleepy-developer.tistory.com/14
- Source: tistory
- Roles: ['backend', 'cs_common', 'devops_infra']
- Published: 2022-05-05T13:31:42+09:00
- Freshness: old
- Rule score: 30
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 비동기 서버의 동작과 주의사항
  - 비동기 서버의 동작과 주의사항

## 113. 아임웹 2차 면접(컬쳐핏) 인터뷰 후기

- URL: https://jamongjjang.tistory.com/218
- Source: tistory
- Roles: ['frontend', 'ai_ml_data', 'backend', 'devops_infra', 'cs_common']
- Published: 2022-06-07T00:28:31+09:00
- Freshness: old
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 저는 프로젝트에서 프론트엔드를 맡아서 하면서, 웹퍼블리싱도 같이 하게 되는데 그때 그러한 미묘한 차이를 경험했고, 장인정신을 발휘하였다고 하였습니다

## 114. 1년차 주니어 프론트 개발자 이직 후기

- URL: https://velog.io/@ohaeseong/1%EB%85%84%EC%B0%A8-%EC%A3%BC%EB%8B%88%EC%96%B4-%ED%94%84%EB%A1%A0%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B4%EC%A7%81-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2021-10-06
- Freshness: old
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 특이했던 것은 지금 껏 코딩 테스트라고 하면 주로 프로그래머스나 백준과 같은 알고리즘을 이용한 문제 해결을 주로 생각하고 준비 해왔는데 카카오 모빌리티에서는 아예 리액트 컴포넌트를 하나 주고 특정 기능을 만드는 것 처럼 완전히 실무적으로 코딩 테스트가 진행 되었습니다

## 115. [UMC] UMC 9기 Spring Boot 서류 + 면접 합격 후기

- URL: https://velog.io/@gthwynn/UMC-UMC-9%EA%B8%B0-%EC%84%9C%EB%A5%98-%EB%A9%B4%EC%A0%91-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2025-09-19
- Freshness: recent
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Spring Boot 파트를 선택한 이유는 무엇인가요?
  - 아직 경험하지 못한 배포, DB 관리, CI/CD, 메시지 큐 등 실무 기술에 도전하려 함
  - DB 사용 경험이 있는지 or 없다면 2주 만에 어떻게 실전 쿼리 작성법을 익힐 것인지
  - 게시글에 해시태그를 여러 개 달 수 있고, 하나의 해시태그가 여러 게시글에 사용될 때, DB 테이블을 어떻게 설계할 것인지
  - API가 무엇이며, REST API란 무엇인지

## 116. 2번째 면접 후기

- URL: https://velog.io/@ddoddiworld/2%EB%B2%88%EC%A7%B8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'frontend', 'cs_common']
- Published: 2024-01-17
- Freshness: recent
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 자바스크립트와 자바나 다른 C같은 언어와의 차이점을 질문 주셨는데 내가 이해를 잘 못해서 답답해 하셨다 ㅠ 결국 정답은 싱글 스레드였는데 설명 해 주셔도 내가 모르는 부분이였기 때문에 당시에 답변을 들어도 잘 이해를 못했을 것 같다

## 117. 3번째 면접 후기

- URL: https://velog.io/@ddoddiworld/3%EB%B2%88%EC%A7%B8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'frontend']
- Published: 2024-02-05
- Freshness: recent
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 타스의 경우, 장단점에 대해 물어보셔서 장점으로는 백엔드(nest.js)에 값을 오류없이(휴먼에러 방지) 넘기고 받기위해서 사용했고 컴파일 돌릴때 미리 이슈를 파악할 수 있다고 설명 드렸다

## 118. DB그룹 계열사 신입사원들이 직접 밝혔다! 면접 질문 및 합격 팁

- URL: https://www.dbblog.co.kr/842
- Source: www.dbblog.co.kr
- Roles: ['unknown']
- Published: 2017-09-06T16:01:08+09:00
- Freshness: old
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - “아직도 직접 일 하세요?” DB Inc

## 119. 소프티어부트캠프 5기 후기, 채용전환까지

- URL: https://gamxong.tistory.com/166
- Source: tistory
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2025-04-28T15:30:46+09:00
- Freshness: recent
- Rule score: 28
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 하지만 저는 이미 백엔드 프로젝트를 5개 정도 경험 한 상태였기 때문에 더 많은 프로젝트를 하기 보다는 기존 프로젝트를 고도화하고 싶은 마음이 컸습니다
  - 저는 그동안 주로 Spring 내부에서 톰캣(Tomcat)이 제공하는 기능을 사용해왔기 때문에 이 프로젝트를 통해 웹서버의 작동 원리를 생각보다 많이 배울 수 있었습니다
  - 앞서 언급한 것처럼, 저는 지금까지 5개의 Spring 프로젝트를 진행하면서 잘 동작하는 서버를 만드는 데는 익숙해졌다고 생각했습니다
  - 뿐만 아니라 RFC 문서에 대해서도 잘 몰랐는데 이 기회로 해당 문서를 보면서 표준 HTTP 스펙에 맞는 웹서버는 무엇인지 깊이있게 알 수 있었습니다

## 120. 온라인마케팅대행사 프론트엔드 신입 면접 후기

- URL: https://domns.tistory.com/entry/%EC%98%A8%EB%9D%BC%EC%9D%B8%EB%A7%88%EC%BC%80%ED%8C%85%EB%8C%80%ED%96%89%EC%82%AC-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%8B%A0%EC%9E%85-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: tistory
- Roles: ['frontend', 'ai_ml_data', 'backend', 'cs_common']
- Published: 2024-06-18T23:56:05+09:00
- Freshness: recent
- Rule score: 28
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - CSR, SSR가 무엇이고 언제 어느걸 쓰는게 좋은지
  - 한마디로 '당신이 프론트엔드 개발자라고 하지만 웹퍼블리셔나 단순 코더가 아니고 개발자라고 할 수 있나?'를 물어보고 싶었던거 같다

## 121. [취준] 백엔드 개발자 신입 첫 면접 후기

- URL: https://velog.io/@seoya_lee/%EC%B7%A8%EC%A4%80-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%8B%A0%EC%9E%85-%EC%B2%AB-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-02-11
- Freshness: recent
- Rule score: 28
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - SQL Injection을 아는지?
  - 포트폴리오에 언급) 쿼리빌더를 제작할 때 어떤 방식으로 했는지?

## 122. 숙명여대 멋쟁이사자처럼 합격 후기(서류, 면접)

- URL: https://velog.io/@wonandonly/%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC-11%EA%B8%B0-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0%EC%84%9C%EB%A5%98-%EB%A9%B4%EC%A0%91
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'frontend']
- Published: 2024-12-12
- Freshness: recent
- Rule score: 28
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 학과 동아리에서 소소한 프로젝트 경험(프론트엔드 담당
  - 백엔드 경험 전무
  - 그동안은 프론트엔드만 경험해봤었기 때문에 백엔드를 경험 해보고 싶었고,
  - 세미나로 백엔드에 대해 배우고 프로젝트 경험도 쌓을 수 있다면 백엔드 경험이 없는 초보자도 기초부터 쌓기 너무 좋을 것 같아서 지원했던 것 같아요
  - 지원 파트(백엔드) 지원 이유, 해당 파트로 어떻게 성장할 것인지 (600자

## 123. 2025년 5월 토스페이먼츠 면접 후기

- URL: https://akku-dev.tistory.com/278
- Source: tistory
- Roles: ['backend', 'devops_infra', 'ai_ml_data', 'cs_common', 'frontend']
- Published: 2025-06-08T16:37:46+09:00
- Freshness: recent
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 최소한 스프링이 내부적으로 어떻게 동작하고, 빈 생명주기, 응답이 만들어지는 과정 정도는 당연히 알아뒀어야 하고 눈 감고도 줄줄 말할 정도가 되어 있었어야 했다

## 124. [2025년 10월] 토스뱅크 백엔드 개발자 직무면접 후기

- URL: https://velog.io/@eddy159/2025%EB%85%84-10%EC%9B%94-%ED%86%A0%EC%8A%A4%EB%B1%85%ED%81%AC-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%A7%81%EB%AC%B4%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2025-11-02
- Freshness: recent
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - MSA 환경에서의 실무 경험 부족
  - 이번 면접을 준비하고 경험하면서 MSA와 대규모 트래픽 처리 에 대한 관심이 생겼습니다
  - 경험이 부족하다면, 토이 프로젝트라도 MSA 환경으로 구성해보면서 직접 부딪혀보려고 합니다

## 125. 신입 웹 퍼블리셔 인성+기술 면접 후기

- URL: https://velog.io/@kyung_99/%EC%8B%A0%EC%9E%85-%EC%9B%B9-%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94-%EC%9D%B8%EC%84%B1%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-08-25
- Freshness: old
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Q: JQuery랑 JavaScript 차이는 무엇인가?
  - Q: 리액트 서버는 무엇을 쓰는지?
  - [CSS] display 속성 block, inline-block, inline 차이점

## 126. [SoMa] 이제서야 쓰는 SW마에스트로 14기 면접 탈락 후기

- URL: https://velog.io/@win-luck/SoMa-%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4-%EB%A7%88%EC%97%90%EC%8A%A4%ED%8A%B8%EB%A1%9C-14%EA%B8%B0-%EB%A9%B4%EC%A0%91-%ED%83%88%EB%9D%BD-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-07-09
- Freshness: recent
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 보너스 질문) REST API 종류?

## 127. SK C&C SKALA 지원 후기

- URL: https://velog.io/@kosssshhhh/SK-CC-SKALA-%EC%A7%80%EC%9B%90-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'devops_infra', 'frontend']
- Published: 2025-01-22
- Freshness: recent
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 나는 기존에 프론트엔드 프로젝트 경험이 많았지만, 산학 프로젝트에서 팀장으로서 Airflow, ETL 파이프라인, 크롤러 작업을 한 경험을 녹여서 작성했다
  - 그리고 인성 질문의 경우 프론트엔드 개발을 집중해서 공부했는데 왜 이 과정에 지원했는지 등의 미리 생각했었던 질문을 받았다
  - 저는 백엔드 위주의 활동만 해왔는데 채용 연계가 안될 경우 너무 얕고 넓은 공부 경험만 생길까 봐 걱정입니다

## 128. [대한항공] 2025년 전문인력 신입/경력 모집 개발IT 부문 전형 후기 (3차 탈락)

- URL: https://velog.io/@hjeongb0320/%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5-2025%EB%85%84-%EC%A0%84%EB%AC%B8%EC%9D%B8%EB%A0%A5-%EC%8B%A0%EC%9E%85%EA%B2%BD%EB%A0%A5-%EB%AA%A8%EC%A7%91-%EA%B0%9C%EB%B0%9CIT-%EB%B6%80%EB%AC%B8-%EC%A0%84%ED%98%95-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['devops_infra', 'backend', 'ai_ml_data', 'cs_common', 'frontend']
- Published: 2025-03-10
- Freshness: recent
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 하지만 프론트 관련으로 말하지 않고 인프라 관련해서 설명해서 넘어갔다

## 129. 코인원, 빗썸 면접 후기

- URL: https://allroundplaying.tistory.com/68
- Source: tistory
- Roles: ['ai_ml_data', 'backend', 'devops_infra', 'cs_common']
- Published: 2018-03-13T17:51:39+09:00
- Freshness: old
- Rule score: 26
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  -  "브랜치, 태그, Git 권한 관리를 어떻게 했는지" 이런 답변이 빠져있다고 한다
  - docker를 이용한 개발(php, java, mysql, oracle 등)   환경 구축 경험 - CI(bamboo, jenkins)를 통한 build, test, deploy 시스템 구축 및   운영 경험 - 형상관리 git, svn 구축 및 운영 경험 - 빌드 과정에 필요한 개발 프로세스 표준화 경험

## 130. [신입 개발자] 기술 면접 질문 정리

- URL: https://velog.io/@hyeeunism/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC
- Source: velog
- Roles: ['unknown']
- Published: 2023-04-06
- Freshness: recent
- Rule score: 26
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - DB모델링을 할때 프로시저를 썼는데 프로시저를 쓴 이유는?

## 131. 넥스터즈 면접에서 00하면 망합니다.

- URL: https://velog.io/@jmjmjmz732002/%EB%84%A5%EC%8A%A4%ED%84%B0%EC%A6%88-%EB%A9%B4%EC%A0%91%EC%97%90%EC%84%9C-00%ED%95%98%EB%A9%B4-%EB%A7%9D%ED%95%A9%EB%8B%88%EB%8B%A4
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common']
- Published: 2023-12-08
- Freshness: recent
- Rule score: 26
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 여기서 치명적인 실수를 하게 되는데, 면접 대비 시간이 부족해서 내가 쓴 기술들은 대충 기억날거라고 여기고(??) CS나 데이터베이스 위주로 평소 모르던 지식들을 공부하며 면접을 준비했다
  - 외부 API 통신 개선을 위해 기존 방식에서 WebClient 비동기 통신으로 변경하셨다고 했는데, Blocking과 Non-Blocking의 차이가 무엇인지
  - 외부 API 테스트 개선 과정에서 외부 API 서버를 mocking하셨다고 했는데 어떻게 구현하셨는지 설명해주세요
  - 꼬리) mock 객체는 자바 안에서 클래스를 따로 만드신걸까요?
  - Reverse Proxy와 SSL을 적용하여 서버 성능과 보안적 부분 개선했다고 하셨는데, Reverse Proxy가 어떻게 성능과 보안에 도움을 주는지 설명해주세요

## 132. 2025 토스 NEXT 백엔드 합격 후기

- URL: https://flight-developer-stroy.tistory.com/106
- Source: tistory
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2025-09-24T16:37:52+09:00
- Freshness: recent
- Rule score: 25
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - APM & 모니터링을 활용하여 Connection Deadlock 해결기   
  - 도 코테 언어가 자바랑 c로 제한이였나요?

## 133. 가비아 클라우드 백엔드 면접 후기 (합격!)

- URL: https://hobo1229.tistory.com/44
- Source: tistory
- Roles: ['backend', 'devops_infra', 'ai_ml_data']
- Published: 2023-04-05T01:12:38+09:00
- Freshness: recent
- Rule score: 25
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 내 자소서나 프로젝트가 대부분 SE나 DevOps 관련된거라 백엔드 역량에 대해 알아보고자 하는것 같기는 했지만, 면접을 보는 내내 클라우드에 대한 질문은 받지 못할 정도로 백엔드 관련 경험만 물어보셨다

## 134. 육군 정보보호병 면접 후기

- URL: https://velog.io/@chj7239/%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EB%B3%91-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'devops_infra']
- Published: 2022-12-09
- Freshness: old
- Rule score: 25
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 서버 보안 점검을 하게 된다면 어떤 취약점이 아직 패치가 덜 되었을 가능성이 가장 높을까요?

## 135. 데브시스터즈 서버 직군은 왜 코딩 면접을 볼까?

- URL: https://tech.devsisters.com/posts/server-position-coding-test/
- Source: tech.devsisters.com
- Roles: ['unknown']
- Published: 2022-06-10
- Freshness: old
- Rule score: 24
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 데브시스터즈 서버 직군은 왜 코딩 면접을 볼까?
  - 데브시스터즈 서버 직군은 왜 코딩 면접을 볼까?

## 136. 첫 면접 후기

- URL: https://velog.io/@junsu930/%EC%B2%AB-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-07-20
- Freshness: recent
- Rule score: 24
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - spring framework는 사용 가능하지만 spring boot나 전자정부 프레임워크는 사용하지 않았어서 그 차이를 좀 메꿀 수 있게 공부해야 할 것 같다
  - pl/sql이란?
  - 전자정부프레임워크와 spring boot의 차이점

## 137. LG전자 최종 합격 후기

- URL: https://velog.io/@gmlstjq123/LG%EC%A0%84%EC%9E%90-%EC%B5%9C%EC%A2%85-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0-988x5k9n
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'frontend']
- Published: 2024-12-24
- Freshness: recent
- Rule score: 24
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 개발은 도전이라는 신념 아래 백엔드, 프론트엔드, AI 등 다양한 분야에서 경험을 쌓으며 변화하는 IT 환경에 빠르게 적응해왔습니다
  - 저 또한 실제로 영어 면접에서 첫 질문이 "What do you do?"였는데, 이 표현의 의미를 잘 몰라서, "I’m sorry but I didn’t understand what you said

## 138. [하나금융TI] 2024년 상반기 신입사원 1차 면접 후기

- URL: https://velog.io/@lemythe423/%ED%95%98%EB%82%98%EA%B8%88%EC%9C%B5TI-2024%EB%85%84-%EC%83%81%EB%B0%98%EA%B8%B0-1%EC%B0%A8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2024-03-22
- Freshness: recent
- Rule score: 24
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 는 내가 어떻게 학습했는지에 대한 모든 설명이 되지 않는다
  - 년 동안 어떻게 학습했는지, 정리해서 말할 수 있도록 준비

## 139. 데브시스터즈 서버 개발자 면접 후기

- URL: https://velog.io/@suunn001/%EB%8D%B0%EB%B8%8C%EC%8B%9C%EC%8A%A4%ED%84%B0%EC%A6%88-%EC%84%9C%EB%B2%84-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2026-01-06
- Freshness: recent
- Rule score: 23
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 단계 온라인 코딩 테스트 알고리즘 및 문제 해결 능력 평가

## 140. SW 마에스트로 16기 합격 후기

- URL: https://velog.io/@mssak/SW-%EB%A7%88%EC%97%90%EC%8A%A4%ED%8A%B8%EB%A1%9C-16%EA%B8%B0-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common']
- Published: 2025-04-07
- Freshness: recent
- Rule score: 23
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 합격자 분들 스펙보면 괴물같으신 분들도 물론 많지만 알고리즘 공부만 열심히 하시고 제대로 된 프로젝트 경험은 없이 이제 막 학습하고 계시는 분들도 간혹 계셨습니다

## 141. CJ올리브영 백엔드개발 면접후기 6명 및 실제 기출 질문답변 50선 자기소개서

- URL: https://www.happycampus.com/intro-doc/38361442/
- Source: www.happycampus.com
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'devops_infra']
- Published: 2026-05-13T15:03:11+09:00
- Freshness: recent
- Rule score: 23
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - Java의 JVM 구조에서 Runtime Data Area의 각 영역별 역할에 대해 설명해 주세요
  - 가비지 컬렉션(GC)의 동작 원리와 대표적인 알고리즘인 G1 GC에 대해 설명해 주세요
  - Java의 인터페이스(Interface)와 추상 클래스(Abstract Class)의 차이점은 무엇인가요?

## 142. 면접후기 + 질문리스트

- URL: https://velog.io/@sarahsea/%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0-%EC%A7%88%EB%AC%B8%EB%A6%AC%EC%8A%A4%ED%8A%B8
- Source: velog
- Roles: ['unknown']
- Published: 2022-01-12
- Freshness: old
- Rule score: 22
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - javascript에서 원시형과 참조형에 대해 설명해달라
  - 주에서 백엔드도 했다던데, 로그인 기능 어떻게 구현했나?

## 143. [에프랩(F-Lab)] Java-Backend 코스 1개월차 후기

- URL: https://velog.io/@jeongbeom4693/%EC%97%90%ED%94%84%EB%9E%A9F-Lab-Java-Backend-%EC%BD%94%EC%8A%A4-1%EA%B0%9C%EC%9B%94%EC%B0%A8-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'cs_common']
- Published: 2025-03-30
- Freshness: recent
- Rule score: 22
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 이전 프로젝트에서 아쉬웠던 부분들을 새로운 관점에서 접근하여 해결해 나가고 있으며, 현재 학습 중인 객체지향 프로그래밍 기법을 적극적으로 적용하려 노력하고 있습니다
  - 단순하게 학습한 이론을 전달하는 것보단 비유를 통해서 상대방에게 설명할 수 있어야 한다

## 144. [스터디] 신입 백엔드 취준생을 위한 모의 면접

- URL: https://velog.io/@leesomyoung/%EC%8A%A4%ED%84%B0%EB%94%94-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%B7%A8%EC%A4%80%EC%83%9D%EC%9D%84-%EC%9C%84%ED%95%9C-%EB%AA%A8%EC%9D%98-%EB%A9%B4%EC%A0%91
- Source: velog
- Roles: ['unknown']
- Published: 2023-06-17
- Freshness: recent
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 면접을 어떻게 준비해야 할 지 모르고, 실전 감각을 기르고 싶은 주니어 백엔드 개발자들에게 많은 도움이 될 것이라고 생각한다

## 145. 스타트업 면접 후기

- URL: https://velog.io/@kimseungho/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%97%85-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2024-11-01
- Freshness: recent
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 테스트와 같은 과정이 실무와 같다면 RDBMS를 설계는 어떻게 진행하는가?

## 146. 학교 현장실습 면접 후기

- URL: https://velog.io/@sujin1018/%ED%98%84%EC%9E%A5%EC%8B%A4%EC%8A%B5-%ED%95%A9%EA%B2%A9
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'cs_common', 'frontend']
- Published: 2022-12-29
- Freshness: old
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드 말고 프론트엔드 개발 시키면 어떻게 할 것인지,

## 147. CEOS 19기 백엔드 합격후기

- URL: https://velog.io/@limbs713/CEOS-19%EA%B8%B0-%EB%B0%B1%EC%97%94%EB%93%9C-%ED%95%A9%EA%B2%A9%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common']
- Published: 2024-03-08
- Freshness: recent
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 기획/디자인/프론트/백엔드 파트의 사람들이 모여 하나의 프로덕션을 출시하는 과정을 경험하는 동아리이다
  - GitHub 링크를 포함하여 개발 경험이나 역량을 보여줄 수 있는 링크를 첨부해 주세요
  - 이를 해결하기 위해 @BatchSize를 통해 toMany 관계의 join을 해결할 수 있으며 toOne 관계에서는 fetch join을 활용해 필요한 데이터를 하나의 쿼리로 조회할 수 있습니다

## 148. 2023 팀네이버 신입 공채 후기 (서류, 코딩테스트, 기술 인터뷰)

- URL: https://velog.io/@shyuuuuni/2023-%ED%8C%80%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%8B%A0%EC%9E%85-%EA%B3%B5%EC%B1%84-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'frontend']
- Published: 2023-06-23
- Freshness: recent
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 본인의 대표적인 개발 경험, 활동을 가장 잘 보여줄 수 있는 Github, 블로그 등의 URL을 작성하시거나 자료를 첨부하시고, 간단한 소개나 설명을 해 주세요
  - 프론트엔드 분야를 선택하고 왜 프론트엔드 개발자가 되고 싶었는지, 그리고 제가 왜 프론트엔드 개발자와 잘 맞는지 위주로 작성했습니다
  - 마지막 4번은 프로젝트별로 기간, Github 주소, 배포 주소, 프로젝트 소개, 팀/개인 프로젝트 여부 등을 간단하게 리스트업해서 설명했습니다

## 149. java 면접 질문 정리 - 1 : 정답 -

- URL: https://velog.io/@hi5004gun/%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EA%B4%80%EB%A0%A8-%EC%A0%95%EB%A6%AC-2
- Source: velog
- Roles: ['unknown']
- Published: 2023-12-28
- Freshness: recent
- Rule score: 20
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - java 언어를 창시한 사람은 누구인가?

## 150. 2022 프로그래머스 데브코스 2기 지원 후기

- URL: https://velog.io/@y005/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%B0%EB%B8%8C%EC%BD%94%EC%8A%A4-2%EA%B8%B0-%EC%A7%80%EC%9B%90-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'devops_infra', 'frontend']
- Published: 2022-03-13
- Freshness: old
- Rule score: 20
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 교육생 선발 과정이기 때문에 지원자인 내가 왜 데브코스에서 진행하는 수업을 받아야 하는지에 대한 이유, 목적(왜 백엔드 개발자가 되려고 하는지)이 명확해야 된다고 생각한다
  - 나의 경우 백엔드 경험을 적는 문항에서는 백엔드 개발과 직접적으로 관련된 웹서비스 배포 경험, 직접적인 웹개발 경험이 아니더라도 AWS 활용, 서버 관리, 데이터베이스 프로그래밍 경험들을 적어서 데브코스에서 다루는 CS분야의 선행 지식이 있다는 걸 어필했다
  - SQL문은 내 기준으로는 완전 기초적인 문제는 아니었고 subquery, join, NULL값 처리와 같은 여러 개념들을 활용해서 해결하는 문제였다
  - 작년 면접 후기와 다르게 백엔드와 관련된 키워드 이야기하면 아는 사람이 손들어서 간단하게 설명하는 걸 진행한게 기억에 남았다

## 151. 프론트엔드 개발자 면접 및 인턴 취업 후기 (=== 직무 전환 후기)

- URL: https://velog.io/@nwejin/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%EB%B0%8F-%EC%9D%B8%ED%84%B4-%EC%B7%A8%EC%97%85-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['frontend', 'backend']
- Published: 2025-01-31
- Freshness: recent
- Rule score: 20
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - css전처리기(scss) 사용 경험
  - RDB 사용 경험

## 152. 비전공자 국비 지원 6개월 과정 후 SI 회사 1년 그리고 퇴사( + 백엔드개발자 신입 면접 후기)

- URL: https://noerror.tistory.com/12
- Source: tistory
- Roles: ['backend', 'cs_common']
- Published: 2023-06-26T13:52:01+09:00
- Freshness: recent
- Rule score: 19
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 본인 현재 퇴사 후 이직관련 면접을 보러 다니며 경험한 바 정장 입고 오라는 업체는 한 군데도 없음) 2) 신입 면접 때 물어본 질문 나는 백엔드 개발자 채용에 지원하였기 때문에 spring과 java 관련 질문이 대부분이었다

## 153. 웹 개발자로 면접 후기

- URL: https://velog.io/@developer119/%EC%9B%B9-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A1%9C-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2021-03-18
- Freshness: old
- Rule score: 19
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 구직중이라 여러 회사에서 면접 제의가 오고 있다, 게임개발을 하면서 간단한 프론트엔드와 백엔드서버를 만저본 경험을 이력서와 포트폴리오에 기재했는데, 그로인해 웹 개발사에서도 면접제의가 온다
  - 싱글페이지 웹가 서버사이드 렌더링의 차이점 및 사용자가 느낄 수 있는 장점 및 단점
  - 자바스크립트는 싱글스레드인데 비동기가 처리 되는 방식에대한 설명

## 154. 중소기업 신입 개발자 면접 후기

- URL: https://velog.io/@yeony402/%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85-%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2024-06-20
- Freshness: recent
- Rule score: 19
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JWT를 사용한 이유가 무엇인가요?
  - Spring 프레임워크에 대해 설명해보세요
  - 어떤 쿼리문 작성했는지..?

## 155. 에프랩 자바 백엔드 1개월 후기

- URL: https://velog.io/@jinkshower/%EC%97%90%ED%94%84%EB%9E%A9-%EC%9E%90%EB%B0%94-%EB%B0%B1%EC%97%94%EB%93%9C-1%EA%B0%9C%EC%9B%94-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend']
- Published: 2024-07-25
- Freshness: recent
- Rule score: 19
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 예를 들어 스프링을 왜 쓰는지에 대해 물어본다면 나는

## 156. (주)더새움 면접 후기/면접 경험 공유 - 사람인

- URL: https://www.saramin.co.kr/zf_user/interview-review?company_nm=(%EC%A3%BC)%EB%8D%94%EC%83%88%EC%9B%80
- Source: saramin
- Roles: ['ai_ml_data', 'backend', 'cs_common']
- Published: 2024-07-09
- Freshness: recent
- Rule score: 18
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - GPT보다 잘 하는 것은 무엇이냐
  - GPT보다 잘 하는 것은 무엇이냐

## 157. 넥스터즈 23기 지원서 후기🤣

- URL: https://bonsik.tistory.com/6
- Source: tistory
- Roles: ['backend', 'cs_common', 'ai_ml_data']
- Published: 2023-06-11T04:43:44+09:00
- Freshness: recent
- Rule score: 18
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 또한, 최근까지 랫플 에서 현직자, 학생 팀원들과 진행했던 사이드 프로젝트에서 git 컨밴션, DTO 생명주기, 예외 관리 등에 대해서 토론하면서 간단히 느낀점과 체계적으로 다시 한번 넥스터즈에서 경험 하고 싶다라는 위주에 내용을 적었습니다
  - 또한 깃허브, 블로그 등을 이용하며 공부했던 방식을 간략히 적었고, 사이드 프로젝트를 진행하면서 이러한 공부 방식이 새로운 기술 학습 간 도움이 됬던 점과 문제 해결에 도움이 됬던 점을 적었습니다

## 158. 2025 현대오토에버 하반기 최종 합격 후기

- URL: https://brorica.tistory.com/287
- Source: tistory
- Roles: ['backend', 'cs_common', 'ai_ml_data', 'devops_infra']
- Published: 2025-10-10T17:08:04+09:00
- Freshness: recent
- Rule score: 18
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - CI/CD, 테스트 코드 등 많은 취준생이 사용하는 키워드를 활용했지만, 실제 업무의 어려움을 해결하는 과정에서 얻은 경험이었기에 구체적인 스토리를 담아 진정성을 높일 수 있었다고 생각합니다

## 159. [취준] 첫 IT직무 면접을 돌아보며

- URL: https://velog.io/@perhona3422/%EC%B7%A8%EC%A4%80-%EC%B2%AB-IT%EC%A7%81%EB%AC%B4-%EB%A9%B4%EC%A0%91%EC%9D%84-%EB%8F%8C%EC%95%84%EB%B3%B4%EB%A9%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-08-04
- Freshness: old
- Rule score: 18
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Spring AOP에 대해 설명해보세요
  - 값을 불러오는 방법에는 'Call by value'와 'Call by reference'가 있는데, Java는 어떤 방식인지 설명해보세요

## 160. 2025년 상반기 재능교육 면접후기 | 51,701 번째 면접경험 - 사람인

- URL: https://www.saramin.co.kr/zf_user/interview-review/detail/idx/51701/%EC%9E%AC%EB%8A%A5%EA%B5%90%EC%9C%A1-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: saramin
- Roles: ['backend', 'ai_ml_data', 'cs_common']
- Published: 2025-04-27
- Freshness: recent
- Rule score: 17
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - node.js 사용 경험

## 161. 신입 백엔드 개발자 취뽀여정 1탄 - 중소(si)기업 면접 후기

- URL: https://velog.io/@kimhyejin67/%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EB%BD%80%EC%97%AC%EC%A0%95-2%ED%83%84-%EC%A4%91%EC%86%8Csi%EA%B8%B0%EC%97%85-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2024-02-03
- Freshness: recent
- Rule score: 17
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - SQL문 얼마나 잘 쓸 줄 아는지?

## 162. [유레카] LG 유플러스 유레카 2기 백엔드 최종 합격 수기

- URL: https://velog.io/@yereumi/LG-%EC%9C%A0%ED%94%8C%EB%9F%AC%EC%8A%A4-%EC%9C%A0%EB%A0%88%EC%B9%B4-2%EA%B8%B0-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%B5%9C%EC%A2%85-%ED%95%A9%EA%B2%A9-%EC%88%98%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'frontend']
- Published: 2025-01-11
- Freshness: recent
- Rule score: 17
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 특히 프로젝트 경험을 통해 프론트엔드 지식의 중요성을 깨달은 점을 이야기하며, 프론트엔드 교육도 포함된 유레카에 지원한 이유를 풀어냈다
  - 그러다 과거에 데이터베이스 해킹을 당했던 경험을 떠올려 이를 잘 풀어내어 작성했다

## 163. 티제이랩스 면접 후기

- URL: https://velog.io/@yeonwoo1125/%ED%8B%B0%EC%A0%9C%EC%9D%B4%EB%9E%A9%EC%8A%A4-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'devops_infra']
- Published: 2022-05-12
- Freshness: old
- Rule score: 16
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 그럼 데이터베이스 설계부터 다하신건가요?
  - 프로젝트 경험이 많지 않고 데이터베이스 설계도 많이 해보지 않아 팀원들과 함께 구현했습니다

## 164. 걍 짧은 푸념글이고 좀 따 지우겠습니다. 신입 프론트엔드 면접 후기 | OKKY 커뮤니티

- URL: https://okky.kr/articles/1035341
- Source: okky.kr
- Roles: ['frontend', 'ai_ml_data', 'backend']
- Published: 2021-08-28T13:59:17
- Freshness: old
- Rule score: 15
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 면접관이 웃으시면서 "HTML ?

## 165. 인생 첫 개발 면접 1트에 성공한 후기 (웹 개발 인턴 합격 수기)

- URL: https://velog.io/@osohyun0224/%EC%9D%B8%EC%83%9D-%EC%B2%AB-%EA%B0%9C%EB%B0%9C-%EB%A9%B4%EC%A0%91-1%ED%8A%B8%EC%97%90-%EC%84%B1%EA%B3%B5%ED%95%B4%EB%B3%B4%EA%B8%B0-%EC%9B%B9-%EA%B0%9C%EB%B0%9C-%EC%9D%B8%ED%84%B4-%ED%95%A9%EA%B2%A9-%EC%88%98%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-12-25
- Freshness: recent
- Rule score: 15
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 개발자 인생을 놓고 보았을 때 저년차에는 프론트 뿐만아니라 백엔드 다 경험해봐야한다고 생각해 이 회사에 지원했고 아직 한달 뿐이지만 많은 기술을 실무에서 배웠습니다

## 166. 웹퍼블리셔 면접 후기

- URL: https://velog.io/@wizwic/%EC%9B%B9%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-09-27
- Freshness: old
- Rule score: 15
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Javascript와 jQuery 얼마나 다룰 줄 아세요?

## 167. 2025 팀네이버 공채 코딩테스트 & 1차 면접 탈락 후기

- URL: https://velog.io/@8804who/2025-%ED%8C%80%EB%84%A4%EC%9D%B4%EB%B2%84-%EA%B3%B5%EC%B1%84-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-1%EC%B0%A8-%EB%A9%B4%EC%A0%91-%ED%83%88%EB%9D%BD-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['cs_common', 'backend']
- Published: 2025-06-21
- Freshness: recent
- Rule score: 15
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 오랫동안 알고리즘을 놓고 있었던 탓에 헤매기는 했지만, 다행히 1시간 30분 정도 만에 3문제 모두 주어진 테스트케이스를 해결하고 반례도 어느 정도 검증한 후 제출을 할 수 있었다

## 168. LG CNS - 실제 면접 질문 126건 확인하기 | 잡코리아

- URL: https://m.jobkorea.co.kr/Start/review/View?C_Idx=160&Half_Year_Type_Code=0&Ctgr_Code=5&FavorCo_Stat=0&G_ID=0&Page=1
- Source: jobkorea
- Roles: ['ai_ml_data', 'backend', 'devops_infra']
- Published: 2026-05-22
- Freshness: recent
- Rule score: 14
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 고객을 직접 응대하며 니즈를 파악하는 업무와 백엔드에서 개발을 하는 업무 중에 무엇을 선호하나요?
  - Guide> 관련학습, 동아리 활동, 수상경험 등을 중심으로 자유롭게 기재해 주시기 바랍니다

## 169. 2022년 하반기 (주)DB하이텍 면접후기 | 41,046 번째 면접경험 - 사람인

- URL: https://www.saramin.co.kr/zf_user/interview-review/detail/idx/41046/%28%EC%A3%BC%29DB%ED%95%98%EC%9D%B4%ED%85%8D-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: saramin
- Roles: ['unknown']
- Published: 2024-07-23
- Freshness: recent
- Rule score: 14
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 년 하반기 (주)DB하이텍 면접후기 | 41,046 번째 면접경험 - 사람인 - 사람인
  - 면접 경험 공유 (주)DB하이텍

## 170. 준비가 정말정말 미흡했던 통화 기술면접 후기;

- URL: https://velog.io/@terria1020/%EC%A4%80%EB%B9%84%EA%B0%80-%EC%A0%95%EB%A7%90%EC%A0%95%EB%A7%90-%EB%AF%B8%ED%9D%A1%ED%96%88%EB%8D%98-%ED%86%B5%ED%99%94-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2023-06-22
- Freshness: recent
- Rule score: 14
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - HTTP 1.0 vs HTTP 2.0 차이
  - 이 중에서 아는 내용(JVM, HTTP, ORM, 인터페이스 vs 추상클래스 차이, 인터프리터 언어 vs 컴파일 언어 차이) 에 대해서는 답변을 했긴 했으나 정말 너무 어리바리하게 대답했고, 모르는 것에 대해서는 패스한 것도 있고 정말 엉망진창으로 면접을 진행했다

## 171. LG CNS 합격 후기: 자소서, 인적성, 면접 질문, 코딩테스트 자세한 팁

- URL: https://jasoseol.com/blog/post/lg-cns-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0-%EC%9E%90%EC%86%8C%EC%84%9C-%EC%9D%B8%EC%A0%81%EC%84%B1-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%90/
- Source: jasoseol.com
- Roles: ['backend', 'ai_ml_data', 'devops_infra']
- Published: 2024-09-11T00:34:03+00:00
- Freshness: recent
- Rule score: 13
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - A) 웹앱을 경험하며 사용했던 PHP/Laravel이라는 백엔드 언어가 한국에서 주로 사용되는 Java에 비해 구시대적인 언어로 치부되고 있음
  - 차 면접은 프로젝트 관련 질문이 많이나오고 클라우드 기반 경험, 예를 들면 MSA, Docker, 쿠버네티스 같은 경험이 있으면 좋습니다

## 172. 🧭 데브코스 백엔드 과정을 시작하며 (데브코스 합격 후기)

- URL: https://velog.io/@byeolhaha/%ED%9A%8C%EA%B3%A0
- Source: velog
- Roles: ['backend', 'frontend', 'ai_ml_data', 'cs_common']
- Published: 2023-05-21
- Freshness: recent
- Rule score: 12
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드 분야로 진출하고자 결심한 이유와 그동안 어떤 노력을 하셨나요?
  - 데브코스에서 어떻게 학습을 계획하고 있나요?

## 173. 프로그래머스 백엔드 데브코스 5기 합격 후기

- URL: https://velog.io/@kkhkr98/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%B1%EC%97%94%EB%93%9C-%EB%8D%B0%EB%B8%8C%EC%BD%94%EC%8A%A4-5%EA%B8%B0-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common', 'frontend']
- Published: 2023-09-08
- Freshness: recent
- Rule score: 12
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 무엇보다 동료학습으로 많은 것을 얻어갈 수 있겠다는 생각이 들었다

## 174. 지마켓 백엔드 면접 후기

- URL: https://velog.io/@guswlsapdlf/%EC%A7%80%EB%A7%88%EC%BC%93-%EA%B8%80%EB%A1%9C%EB%B2%8C-%EB%B0%B1%EC%97%94%EB%93%9C-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['unknown']
- Published: 2022-09-16
- Freshness: old
- Rule score: 11
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 자기 소개 과정에서 github에 public repository에 올려 둔 프로젝트가 있다고 언급했었는데 그 github을 보시고 "이 코드를 이렇게 작성한 이유가 무엇인지?"라는 질문을 받았었다

## 175. 나의 첫 개발회사 면접 후기(바로고 인턴 면접)

- URL: https://velog.io/@klqwrx7004/%EB%82%98%EC%9D%98-%EC%B2%AB-%EA%B0%9C%EB%B0%9C%ED%9A%8C%EC%82%AC-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0%EB%B0%94%EB%A1%9C%EA%B3%A0-%EC%9D%B8%ED%84%B4-%EB%A9%B4%EC%A0%91
- Source: velog
- Roles: ['unknown']
- Published: 2022-03-30
- Freshness: old
- Rule score: 11
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 파이썬과 자바스크립트를 둘다 해보면서 느꼈던 차이점은 무엇인지?
  - 자바스크립트를 하면서 async/await을 활용하였다고 하였는데 이 async/await을 왜 쓰는건지?
  - 마지막으로 공통질문을 하셨는데 Rest API 에 대해 자유롭게 설명해보시라고 하셨다

## 176. 프로그래머스 데브코스 3기 면접 후기

- URL: https://velog.io/@sejun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%B0%EB%B8%8C%EC%BD%94%EC%8A%A4-3%EA%B8%B0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'cs_common', 'frontend']
- Published: 2022-10-23
- Freshness: old
- Rule score: 11
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 해당 선택을 하는데는 7월에 경험했던 해커톤 경험이 주효하게 작용했는데, 처음으로 학과 동기들이 아닌 다른사람과의 협업을 진행하는 대학공동해커톤을 진행하면서 프론트엔드개발에 주도성이 없는것 같다는 생각을 가지게 되어, 수동적인 개발이 아닌 좀더 주도적인 개발이 하고 싶다는 생각이 들었기 때문이다

## 177. 신입 개발자 취업 후기 (면접팁)

- URL: https://velog.io/@krhopy/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EC%97%85-%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91%ED%8C%81
- Source: velog
- Roles: ['unknown']
- Published: 2023-01-16
- Freshness: recent
- Rule score: 10
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - python과 java의 차이점 ( 둘다 공부를 했어서 질문이 들어왔어용
  - svn 과 github 차이 ( 둘다 써봤어서 물어보심

## 178. SK AX SKALA 2기 지원 후기 (SKCT, 면접)

- URL: https://velog.io/@andro606/SK-AX-SKALA-2%EA%B8%B0-%EC%A7%80%EC%9B%90-%ED%9B%84%EA%B8%B0-SKCT-%EB%A9%B4%EC%A0%91
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'frontend']
- Published: 2025-07-11
- Freshness: recent
- Rule score: 10
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 프론트엔드 중심의 프로젝트 경험은 많았지만, 졸업을 앞두고 ‘나만의 경쟁력’에 대해 고민하게 되었습니다
  - AI/데이터 분석 경험 : 백엔드와 서버를 제대로 경험한적이 없었기에 학부 수업중 데이터 시각화 관련된 내용을 기술

## 179. 멋쟁이사자처럼 서류 및 면접 최종 합격 후기

- URL: https://velog.io/@3eonah/%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC-%EC%84%9C%EB%A5%98-%EB%B0%8F-%EB%A9%B4%EC%A0%91-%EC%B5%9C%EC%A2%85-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['ai_ml_data', 'backend', 'frontend']
- Published: 2023-03-19
- Freshness: recent
- Rule score: 10
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 파트 선택 이유와 관련 경험은, 좌쪽에 있는 '프론트엔드의 일' 을 바탕으로 작성했습니다
  - 프론트엔드 파트와 백엔드 파트의 차이에 대해 말씀해주세요

## 180. 2023년 현대오토에버 면접 후기, 최종 합격 비결 모음.zip

- URL: https://jasoseol.com/blog/post/review_hyundaiauto_240116/
- Source: jasoseol.com
- Roles: ['backend', 'devops_infra']
- Published: 2024-07-23T12:24:57+00:00
- Freshness: recent
- Rule score: 9
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 기술적인 검증이 다 끝난 뒤에 기술을 바라보는 가치관을 묻는 질문으로 “백엔드란 무엇인가”라는 질문이 매우 좋았습니다

## 181. 한미약품(주) - 인적성 검사 후기 19건 확인하기 | 잡코리아

- URL: https://www.jobkorea.co.kr/starter/review/view?c_idx=391&ctgr_code=2
- Source: jobkorea
- Roles: ['ai_ml_data', 'backend', 'cs_common', 'frontend']
- Published: 2016-09-06
- Freshness: old
- Rule score: 9
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 저는 컴퓨터 소프트웨어공학을 전공하며 프론트엔드와 웹 백엔드 모두 경험했습니다

## 182. 2021 가비아 백엔드 개발자 면접까지 후기

- URL: https://kkyu67.tistory.com/entry/2021-%EA%B0%80%EB%B9%84%EC%95%84-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%EA%B9%8C%EC%A7%80-%ED%9B%84%EA%B8%B0
- Source: tistory
- Roles: ['unknown']
- Published: 2022-01-04T09:23:25+09:00
- Freshness: old
- Rule score: 9
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드에 병특 경험이 어떻게 도움이 될 수 있는지

## 183. NEXTERS 25기 합격후기

- URL: https://velog.io/@junho5336/NEXTERS-25%EA%B8%B0-%ED%95%A9%EA%B2%A9%ED%9B%84%EA%B8%B0
- Source: velog
- Roles: ['backend', 'ai_ml_data', 'cs_common']
- Published: 2024-06-05
- Freshness: recent
- Rule score: 9
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 기술 면접에서는 평소에 기술을 사용할 때 새로 학습한 내용을 블로깅하면서 내 생각을 정리했던 경험이 많은 도움이 되었다

## 184. [Java] 첫 면접 스터디 후기 & 질문 모음

- URL: https://velog.io/@nhe0622/Java-%EC%B2%AB-%EB%A9%B4%EC%A0%91-%EC%8A%A4%ED%84%B0%EB%94%94-%ED%9B%84%EA%B8%B0-%EC%A7%88%EB%AC%B8-%EB%AA%A8%EC%9D%8C
- Source: velog
- Roles: ['unknown']
- Published: 2024-12-02
- Freshness: recent
- Rule score: 8
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 가비지 컬렉션이 어떻게 작동하는지와 그 알고리즘에 대해서 설명하세요
  - Java가 컴파일되는 과정에 대해 설명하세요
  - 자바의 주요 특징에 대해 설명하세요

## 185. [LG CNS] 23년 하반기 2차 면탈 후기

- URL: https://velog.io/@lemythe423/LG-CNS-23%EB%85%84-%ED%95%98%EB%B0%98%EA%B8%B0-%EC%8B%A0%EC%9E%85-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8
- Source: velog
- Roles: ['backend']
- Published: 2023-10-08
- Freshness: recent
- Rule score: 5
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 백만 크기의 2차원 배열을 선언해서 풀었다가 defaultdict으로 바꿨는데 어떻게 풀어도 시간초과는 안 날 문제였다고 생각한다

## 186. 나이스피앤아이(주) 인적성·면접후기 - 모든 취업후기를 한눈에 확인 | 잡코리아 신입공채

- URL: https://www.jobkorea.co.kr/company/1415218/Review
- Source: jobkorea
- Roles: ['ai_ml_data', 'backend', 'cs_common', 'frontend']
- Published: None
- Freshness: unknown
- Rule score: -6
- Rule reason: 실제 면접 신호와 구체 기술 질문 후보가 있음
- Rule question samples:
  - 알고리즘 문제를 많이 풀었는데 다른 기업에는 어떻게 보셨는지?
