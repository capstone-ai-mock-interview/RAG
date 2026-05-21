# ChatGPT 수동 검수 프롬프트

아래 후보들은 규칙 기반 크롤링 실사에서 A등급으로 분류된 문서입니다.
AI 모의면접 RAG Knowledge Base에 넣을 수 있는지 A/B/C/D로 재분류해주세요.

등급 기준:
- A: 실제 기업 면접 후기이며, 실제로 받은 백엔드/CS 기술 질문이 3개 이상 있음
- B: 실제 기업 면접 후기지만 질문이 적거나, 회사/개인 프로젝트 맥락이 강해 일반화가 어려움
- C: 실제 후기는 아니지만 기술 면접 질문 은행/가이드로 보조 활용 가능
- D: 광고, 강의/멘토링 홍보, 동아리/부트캠프 면접, 개인 회고/답변문, 비기술 질문, 노이즈

주의:
- 자기소개, 지원동기, 마지막 질문, 회사 위치/조직 관련 질문은 백엔드 기술 질문으로 세지 마세요.
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
      "usable_questions": ["실제로 쓸 수 있는 백엔드/CS 기술 질문만"]
    }
  ]
}
```

검수 대상:

## 1. 백엔드 개발자 [면접/학습내용]

- URL: https://velog.io/@minsgy/%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%ED%95%99%EC%8A%B5%EB%82%B4%EC%9A%A9
- Source: velog
- Published: 2021-01-07
- Rule score: 110
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 일반적으로 설명하는 DNS Lookup은 루트 도메인서버에서부터 서브도메인 서버순으로 찾게됩니다
  - TCP와 UDP의 차이점에 대해서 설명해보세요
  - TCP 3, 4 way handshake에 대해서 설명해보세요
  - TCP를 공부하셨다면 이 정도는 알겠지 하고 묻는 문제고, 실제 면접자리에서는 보통 네트워크에 대해서 설명할 때, 직접 설명하는 편입니다
  - HTTP와 HTTPS의 차이점에 대해서 설명해보세요

## 2. 신입 백엔드 면접 질문 Ver. 2.0.7

- URL: https://velog.io/@yukina1418/%EC%B5%9C%EA%B7%BC-%EB%A9%B4%EC%A0%91%EC%9D%84-%EB%8B%A4%EB%8B%88%EB%A9%B4%EC%84%9C-%EB%B0%9B%EC%95%98%EB%8D%98-%EC%A7%88%EB%AC%B8%EB%93%A4
- Source: velog
- Published: 2022-06-29
- Rule score: 92
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - In-memory DB에 대해서 설명해주세요
  - Redis를 사용하신 이유가 무엇인가요?
  - Redis와 Memcached의 차이를 이야기해주세요
  - Redis를 비전공자에게 설명해준다고 생각하고 이야기해주세요
  - Redis의 단점은 무엇이 있을까요?

## 3. 개발자 경력직 기술면접, 준비, 뒤늦은 후기

- URL: https://mellowp-dev.tistory.com/4
- Source: tistory
- Published: 2019-10-03T15:00:33+09:00
- Rule score: 88
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 알고리즘 관련해서 정리를 잘해놓은 블로그가 많아 공부하기 편했고, 코딩 테스트를 해볼수 있는 사이트에서 실전(?) 도 여러번
  - 추가로 과제에서 JPA 를 사용할 계획이 있는지, TDD 코드도 추가 할건지 ?
  - H2 DB 를 사용할건지 ?
  - 타 팀과 연동작업을 할때 API 문서는 어떤식으로 작성하고 관리 했는지를 물어보았다
  - 위와 같이 경험했던 내용을 말했고,  swagger 를 사용할때가 개인적으로 좋았다고 말씀드리며 기회가 되면 Spring Rest Docs 도 해보고 싶다고 나름 어필(?) 하였다

## 4. [면접] Spring 및 백엔드 질문리스트

- URL: https://velog.io/@tjddnths0223/%EB%A9%B4%EC%A0%91-Spring-%EB%B0%8F-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%A7%88%EB%AC%B8%EB%A6%AC%EC%8A%A4%ED%8A%B8
- Source: velog
- Published: 2022-10-11
- Rule score: 88
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JPA는 무엇인가
  - 그리고 객체지향 프로그래밍은 클래스를 사용하고 RDBMS는 테이블을 사용하는데 이 모델 간에 불일치가 존재하는데, 이런 패러다임 불일치를 해결해준다
  - Spring Framework와 Spring Boot의 차이
  - Spring Web MVC의 Dispatcher Servlet 동작원리
  - Spring Bean Life Cycle에 대한 설명

## 5. [SW마에스트로 15기]얻은 것이 많은 심층 면접 탈락자의 회고

- URL: https://velog.io/@alswp006/SW%EB%A7%88%EC%97%90%EC%8A%A4%ED%8A%B8%EB%A1%9C-15%EA%B8%B0%EC%96%BB%EC%9D%80-%EA%B2%83%EC%9D%B4-%EB%A7%8E%EC%9D%80-%EC%8B%AC%EC%B8%B5-%EB%A9%B4%EC%A0%91-%ED%83%88%EB%9D%BD%EC%9E%90%EC%9D%98-%ED%9A%8C%EA%B3%A0
- Source: velog
- Published: 2024-03-22
- Rule score: 83
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 크롬 확장 프로그램은 불편함을 개선하기 위해 만들었고 성공적으로 배포까지 해보았다는 것을 적었고 알고리즘 스터디는 제가 직접 만들어 스터디 계획, 스터디 과정을 그렇게 계획한 이유를 차근차근 설명하며 적었습니다
  - 생활 속에서 문제를 해결하기 위해 알고리즘 적용해본 사례가 있는지?
  - RESTful API란?
  - RESTful API의 장단점
  - REST API 종류?

## 6. 8월 캠프콘 후기 : 기술 면접관이 알려주는 백엔드 기술 면접 합격 A to Z

- URL: https://velog.io/@socra/8%EC%9B%94-%EC%BA%A0%ED%94%84%EC%BD%98-%ED%9B%84%EA%B8%B0-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91%EA%B4%80%EC%9D%B4-%EC%95%8C%EB%A0%A4%EC%A3%BC%EB%8A%94-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%ED%95%A9%EA%B2%A9-A-to-Z
- Source: velog
- Published: 2024-08-31
- Rule score: 81
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드 개발이란?
  - 백엔드 개발자는 Application이 어떻게 데이터를 처리하고, 사용하는지 가장 잘 알고 있습니다
  - 💡 데이터베이스의 인덱스에 대해 설명해주세요
  - 모호한 문제 설명, 비체계적인 접근: 한 번 서버가 느려진 적이 있었는데, 원인을 찾기가 어려웠어요
  - 결국엔 서버를 재시작했더니 문제가 해결됐습니다

## 7. [면접총정리] 신입 개발자 인터뷰 대비 총정리 자료 - ⑤ 운영체제

- URL: https://hoons-dev.tistory.com/95
- Source: tistory
- Published: 2022-10-31T14:38:50+09:00
- Rule score: 80
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Java 를 사용하지 않는다면, 자신의 직무 언어 및 프레임워크 관점에서 문제를 해결해보는 것을 추천합니다
  - 💡 OS(운영체제)가 무엇인지 설명해주실 수 있나요?
  - + 동기화가 무엇인지 Java 챕터에서 참고
  - 💡 Race Condition과 Critical Section이 무엇이고, 경쟁상태를 막기 위해 어떤 방법을 사용하는지 설명해주세요
  - 💡 페이지 교체가 언제 발생하는지, 어떤 교체 알고리즘이 있는지 설명해주세요

## 8. SPRING 면접 질문

- URL: https://velog.io/@winckey0/SPRING-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8
- Source: velog
- Published: 2022-11-07
- Rule score: 76
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 스프링에서 AOP가 뭔가요?
  - MVC에 대해서 설명해주세요
  - JPQL에서 동작한 쿼리를 통해서 members에 데이터가 바인딩 됩니다
  - 이미 영속성 컨텍스트에 들어있기 때문에 따로 쿼리가 실행되지 않은 채로 N+1문제가 해결됨
  - 자바 컬렉션 List, set, map에 대한 설명

## 9. 위코드 수료 후 백엔드 면접 후기 및 FAQ1 - 기술면접 · Lunallena TIL Blog

- URL: https://lunayyko.github.io/wecode/2021/10/27/interview1/
- Source: lunayyko.github.io
- Published: None
- Rule score: 75
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JWT는 무엇인가?
  - JWT를 왜 사용하였는지?
  - JWT의 변조 알고리즘에는 무엇이 있는지?
  - JWT가 어떤 방식의 해킹을 당할 수 있는지 그리고 그걸 예방하기 위해서 어떻게 해야하는지?
  - Eager Loading은 무엇인가?

## 10. 엘리스 면접 특강을 돌아보며 (feat. 백엔드)

- URL: https://velog.io/@malza_0408/%EC%97%98%EB%A6%AC%EC%8A%A4-%EB%A9%B4%EC%A0%91-%ED%8A%B9%EA%B0%95%EC%9D%84-%EB%8F%8C%EC%95%84%EB%B3%B4%EB%A9%B0
- Source: velog
- Published: 2022-08-14
- Rule score: 61
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 멱등성을 보장하는 REST method?
  - 🔥✅ HTTP와 HTTPS의 차이?
  - 🔥✅ HTTP를 사용하는 REST API 서버에게 HTTPS를 사용하게 하기 위해서는 어떠한 절차를 거쳐야 하는지?
  - HTTP -> TCP -> 패킷의 흐름까지 이해하고 설명 할 수 있으면 훌륭하다
  - HTTP 연결을 맺을 때 수행되는 TCP Three-way-handshake와 HTTPS 연결을 맺을 때 수행되는 TLS handshake를 설명할 수 있으면 좋다

## 11. [SKT Devocean Young] JPA 도서 스터디 후기

- URL: https://velog.io/@jiww4/SKT-Devocean-Young-JPA-%EB%8F%84%EC%84%9C-%EC%8A%A4%ED%84%B0%EB%94%94-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2024-11-30
- Rule score: 61
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JPA란 JPA(Java Persistence API)는 자바 개발자에게 객체와 관계형 데이터베이스 간의 매핑을 지원하는 ORM 기술 표준으로, 애플리케이션과 JDBC 사이에서 동작
  - +) ORM(Object-Relational Mapping) 객체와 관계형 데이터베이스 간의 패러다임 불일치를 해결하기 위해 객체와 테이블을 매핑하며, JPA는 SQL 작성 및 변환 작업을 대신 처리해 개발자의 부담을 줄임
  - JPA의 간단한 동작 원리객체 저장 시 SQL을 자동 생성하여 데이터베이스에 저장하고, 조회 시 객체 그래프를 탐색하며 필요한 데이터를 적절히 조회
  - H2 오류 해결H2 데이터베이스를 사용할 경우, 파일 경로(예: Users/user/test test.mv.db)가 올바르게 설정되어 있는지 확인
  - 플러시와 트랜잭션플러시는 영속성 컨텍스트의 변경 내용을 데이터베이스에 반영하며, 트랜잭션 커밋, JPQL 실행, flush() 호출 시 동작

## 12. [면접후기] 8/30 매칭데이

- URL: https://velog.io/@hjh3933/%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0-830-%EB%A7%A4%EC%B9%AD%EB%8D%B0%EC%9D%B4
- Source: velog
- Published: 2024-09-02
- Rule score: 59
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 질문: restful api에 대해 설명해달라고 하심
  - 질문: 입사하면 고객처에 서버 설치도 해야하는데 할 수 있는지?
  - 질문: node.js랑 spring중에 뭐가 더 자신있는지?
  - 질문: 데이터베이스 설계 해본 경험 있는지?
  - 회사 스택을 찾아보고 미리 검색하고 가는게 도움이 많이 되었음, 사실 nest.js로 이번에 처음 들었는데 node.js 관련 프레임워크라고 해서 아하 그렇구나 하고 알고 갔더니 nest.js로 사용해본적 있냐는 질문에 사용경험은 없지만 node.js를 많이 사용해보아서 금방 익힐 수 있을 것 같다고 답변할 수 있었음

## 13. [면접] 기술면접 질문 및 후기 정리

- URL: https://esther99.tistory.com/44
- Source: tistory
- Published: 2024-04-09T16:41:13+09:00
- Rule score: 58
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JPA와 Querydsl은 명확한 차이가 있을텐데 어떤 차이가 있고, 어떤 점이 좋았는지?
  - 백엔드를 선택한 이유는?
  - HTTP에서 get과 post 통신의 차이를 아는지?

## 14. [기술면접] Spring 면접질문 (3)

- URL: https://velog.io/@rdamin/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-Spring-%EB%A9%B4%EC%A0%91%EC%A7%88%EB%AC%B8-3
- Source: velog
- Published: 2025-01-02
- Rule score: 56
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - POJO란 무엇인가, Spring Framework에서 POJO는 무엇이 될 수 있을까?
  - RESTFul이란 무엇인지, 아는대로 설명하시오
  - 서버-클라이언트 구조: 서버와 클라이언트가 독립적으로 동작하며, HTTP를 통해 상호작용합니다
  - 긴급 상황에서는 우선 스케일 아웃과 캐시 적용 등 단기적인 해결책에 집중하고, 이후 장기적으로 로드 밸런서와 DB 최적화를 진행합니다
  - 어떻게 쿼리가 실행될까?

## 15. JAVA 신입 1차 면접 질문

- URL: https://velog.io/@aleydis/JAVA-%EC%8B%A0%EC%9E%85-1%EC%B0%A8-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8
- Source: velog
- Published: 2020-09-03
- Rule score: 54
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 데이터베이스에는 어떤 테이블이 있었고, 각 테이블의 컬럼은 뭐가 있었나요?
  - 프로젝트에서 mvc 패턴을 어떻게 구성했는지
  - MVC Model1과 Model2의 차이
  - TCP/UDP 차이
  - 기억에 남는 알고리즘 문제는 무엇인가?

## 16. 신입 개발자 기술면접 질문 정리 - 자바

- URL: https://velog.io/@kallis0926/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC-%EC%9E%90%EB%B0%94
- Source: velog
- Published: 2023-12-20
- Rule score: 53
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 💡 Java의 특징을 설명해주세요
  - JVM(자바가상머신) 위에서 동작하기 때문에 운영체제에 독립적이다
  - JVM은 스택 기반으로 동작하며, Java Byte Code를 OS에 맞게 해석 해주는 역할을 하고 가비지컬렉션을 통해 자동적인 메모리 관리를 해줍니다
  - 💡 Java의 컴파일 과정에 대해 설명해주세요
  - 💡 Java에서 제공하는 원시 타입들은 무엇이 있고 각각 몇 바이트를 차지하는가?

## 17. 첫 프론트엔드 인턴 면접 후기[면접탈]

- URL: https://velog.io/@kwak1539/%ED%98%84%EC%9E%A5%EC%8B%A4%EC%8A%B5-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%9D%B8%ED%84%B4-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2022-11-30
- Rule score: 52
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 프론트엔드 말고도 백엔드 경험이 있는지?
  - JavaScript 말고 다른 언어를 사용해본 적이 있는지?
  - JavaScript의 Promise에 대해 설명할 수 있는지?
  - React를 사용하면서 기존 Vanilla JavaScript와 비교해서 어떤 점이 좋았는지 구체적으로 설명할 수 있는지?
  - 알고리즘 문제는 Python말고 JavaScript로는 풀어본 경험이 있는지?

## 18. 신입 개발자 기술 면접 질문 - Java

- URL: https://velog.io/@xangj0ng/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-Java
- Source: velog
- Published: 2023-02-12
- Rule score: 52
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Java의 특징을 설명해주세요
  - JVM(자바가상머신) 위에서 동작하기 때문에 운영체제에 독립적이다
  - JVM은 스택 기반으로 동작하며, Java Byte Code를 OS에 맞게 해석 해주는 역할을 하고 가비지컬렉션을 통해 자동적인 메모리 관리를 해줍니다
  - Java의 컴파일 과정에 대해 설명해주세요
  - 불변 객체가 무엇인지 설명하고 대표적인 Java의 예시를 설명해주세요

## 19. [후기] 면접 후기

- URL: https://velog.io/@yaaloo/%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-06-02
- Rule score: 51
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - MariaDB에 부분 문자열 검색 기능이 있는데, 그건 왜 거르고 ES를 사용했는가?
  - 왜냐면, jwt 자체가 약간의 보안을 희생하고 효율성을 높이기 위한 기술이기 때문에 엑세스 토큰은 저장을 하지 않고 리프레시 토큰만을 저장하게끔 설계를 했다
  - 매 요청 시마다 세션 스토리지를 조회함으로써 서버 부하를 늘리는 것이 세션 방식의 문제 중 하나인데, 매번 세션 값을 찾는거나, 사용자의 현재 jwt 값을 찾는거나 과연 다를 게...?
  - 단점은 이전 사용자를 로그아웃 시키기 위해서는 엑세스 토큰을 db에 저장해두고 매 요청마다 일치하는지 확인해야 한다는 것?
  - MariaDB에 부분 문자열 검색 기능이 있는데, 그건 왜 거르고 ES를 사용했는가?

## 20. [취준 기록] 신입 백엔드 개발자 면접 후기 (기술면접, 인성면접, 최종면접)

- URL: https://ddooroong.tistory.com/entry/%EC%B7%A8%EC%A4%80-%EA%B8%B0%EB%A1%9D-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%9D%B8%EC%84%B1%EB%A9%B4%EC%A0%91-%EC%B5%9C%EC%A2%85%EB%A9%B4%EC%A0%91
- Source: tistory
- Published: 2023-07-22T12:56:27+09:00
- Rule score: 50
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - github에 작성한 내용 중에서) session으로 권한을 구분했다고 되어있는데, 더 자세히 설명해주세요
  - Spring 사용해보았는지?
  - Spring을 사용했을 때와 사용하지 않았을 때 본인이 느낀 점은 무엇인지?
  - 데이터베이스 프로젝트에서 테이블은 총 몇 개가 나왔는지?
  - DB 쿼리문은 잘 다루는 편인지?

## 21. [취업] 2022 하반기 백엔드 취업회고 : 14번의 면접 그리고 취뽀 - 4 (기술면접)

- URL: https://velog.io/@rmswjdtn/%EC%B7%A8%EC%97%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%8B%A0%EC%9E%85-14%EB%B2%88%EC%9D%98-%EB%A9%B4%EC%A0%91-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%B7%A8%EB%BD%80-4-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91
- Source: velog
- Published: 2023-02-25
- Rule score: 50
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 이 강의는 뭔가 이론적으로만 딱딱하게 배웠던 네트워크 개념을 좀더 와닿게(?) 설명해주신다
  - 면접때 Spring도 준비해야하는 분들을 위해서 공부팁을 조금 더 붙이자면 Spring의 동작원리 (?)에 대해서 깊게 이해하는 것이 좋다
  - 특히 나처럼 Spring 프로젝트 경험이 있고 그것을 서류에 썼다면 무조건 공부해야하며 다른 프레임워크를 썼던 분들은 당연히 해당 프레임워크에 대해 깊이 공부하고 가는 것이 좋다
  - 혹시 자바 스프링 학습 기간은 어느정도 되셨고 어느정도 시간을 투자하셨는지 알 수 있을까요?

## 22. [취준 기록] 신입 백엔드 개발자 면접 / 기술면접 후기

- URL: https://ddooroong.tistory.com/entry/%EC%B7%A8%EC%A4%80-%EA%B8%B0%EB%A1%9D-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: tistory
- Published: 2023-07-13T12:55:02+09:00
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 프론트엔드 / 백엔드 / 풀스텍 중에서 본인이 하고자 하는 역할은?
  - 백엔드 개발에 더 관심이 있는 이유는?
  - REST API 사용 경험
  - Spring 프로젝트에서 데이터베이스는 어떤걸 사용했는지?
  - 자바 스크립트에서 변수 var, let, const에 대해서 설명

## 23. [기술면접] Spring 면접질문 (2)

- URL: https://velog.io/@rdamin/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-Spring-%EB%A9%B4%EC%A0%91%EC%A7%88%EB%AC%B8-2
- Source: velog
- Published: 2024-12-31
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - DI가 뭔지 객체지향관점을 연결지어 말하기
  - JWT(Json Web Token)에 대해 간단히 설명
  - OAuth에 대해 간단히 설명해주세요
  - JWT와 OAuth의 차이는 무엇이 있을까요?
  - 저희 프로젝트에서는 프론트엔드(Vue.js) 와 백엔드(Spring Boot) 가 서로 다른 도메인에서 동작하고 있었고, 예를 들어 프론트엔드는 http://localhost:5173 , 백엔드는 http://localhost:8080에서 실행되었습니다

## 24. 📒 기술면접 정리 ( Spring )

- URL: https://velog.io/@rlaghwns1995/%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A0%95%EB%A6%AC-Spring
- Source: velog
- Published: 2021-10-12
- Rule score: 48
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 스프링 프레임워크란 ?
  - MVC 구조란 ?
  - DispatcherServlet이란 ?
  - 반대로 말하면 스프링에게 애플리케이션의 흐름을 제어하는 권한(IoC)이 없다면?

## 25. 부트캠프 수료 후 1년만에 개발자 취업 후기 및 2024 회고

- URL: https://velog.io/@ystar5008/%EB%B6%80%ED%8A%B8%EC%BA%A0%ED%94%84-%EC%88%98%EB%A3%8C-%ED%9B%84-1%EB%85%84%EB%A7%8C%EC%97%90-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EC%97%85-%ED%9B%84%EA%B8%B0-%EB%B0%8F-2024-%ED%9A%8C%EA%B3%A0
- Source: velog
- Published: 2025-01-03
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - "프로젝트에서 JWT 토큰을 사용하셨는데 그 이유가 뭔가요?" 라는 질문이 날아왔다
  - "자바스크립트에서 배열과 객체의 차이가 무엇인가요?"
  - 면접 질문 정리: https://lively-quokka-d71.notion.site/153480a3853d80a4bd25ed412b516d7f?pvs=

## 26. 🎞️휴맥스 드림버스컴퍼니 지원&면접 후기

- URL: https://velog.io/@dlgkdis801/%ED%9C%B4%EB%A7%A5%EC%8A%A4-%EB%93%9C%EB%A6%BC%EB%B2%84%EC%8A%A4%EC%BB%B4%ED%8D%BC%EB%8B%88-%EC%A7%80%EC%9B%90%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-10-19
- Rule score: 44
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - OO 서버는 어떤 로직으로 구성했나요?
  - OO 클래스와 OO 알고리즘은 어떻게 이용했나요?
  - Spring, SpringBoot, SpringSecurity에 대해서 설명해보세요
  - Redis는 어떤 DB인지 설명해주실래요?
  - Github, Postman, AWS는 어느 정도로 사용이 가능하신가요?

## 27. 신입 개발자 기술면접 질문 리스트

- URL: https://velog.io/@harry__/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8
- Source: velog
- Published: 2023-12-14
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 💡 Java의 특징을 설명해주세요
  - JVM(자바가상머신) 위에서 동작하기 때문에 운영체제가 독립적이다
  - JVM은 스택 기반으로 동작하며, Java Byte Code를 OS에 맞게 해석 해주는 역할을 하고 가비지컬렉션을 통해 자동적인 메모리 관리를 해준다
  - 💡 Java의 컴파일 과정에 대해 설명해주세요
  - 💡 Java에서 제공하는 원시 타입들에 무엇이 있고, 각각 몇 바이트를 차지하나요?

## 28. 20220103 면접후기

- URL: https://velog.io/@jihye/20220103-%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2022-01-03
- Rule score: 43
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 프로젝트에서 어떤 기능을 맡아서 개발하였는지, 사용한 라이브러리는 어떤 것이 있는지같이 예상 가능한 질문들도 있었고, 지난번 모의 면접때처럼 http와 https의 차이는 무엇인지 아는지 물어보셨다
  - 여러 분야중 왜 백엔드를 선택했는지에 대한 질문도 하셨다
  - JAVA란 무엇일까?

## 29. [회고] 2024 SSAFY 공통 프로젝트 - "Speechless" 회고

- URL: https://velog.io/@cloud_365/%ED%9A%8C%EA%B3%A0-2024%EB%85%84-SSAFY-%EA%B3%B5%ED%86%B5-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0
- Source: velog
- Published: 2024-02-18
- Rule score: 42
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Transaction 문제는 해결했으나 openVidu 서버로 요청을 보내는 과정에서 위 에러가 발생했다
  - 결국 openVidu 포트로 접속해 이미 등록된 인증서를 가져와 keytools를 가지고 JAVA에 인증서를 추가하고 문제가 해결됐다

## 30. 2차 면접 후기 정리

- URL: https://velog.io/@god0478/2%EC%B0%A8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0-%EC%A0%95%EB%A6%AC
- Source: velog
- Published: 2024-10-25
- Rule score: 42
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 기술면접에서 물어보셨던게 일단 프로젝트 관련해서 jwt header 말로 다른 방법으로 보낼 수있는 방법이 있을까요?
  - 하 전에 배웠던 개념이긴한데 조금 오래되서 의존개념이 내가 직접 주입하냐 스프링이 주입하냐에 차이인데 간단하게 내가 주입하게 될 경우 라이플 사이클이냐 객체 생성을 직접해야 되기때문에 코드가 길어질 수 있고 이걸 스프링이 해주게되면 코드도 줄어들고 라이프사이클을 알아서 관리해준다

## 31. 2024 미래내일 일경험 IT 백엔드 개발자 면접 후기

- URL: https://eod940.tistory.com/55
- Source: tistory
- Published: 2024-05-18T22:04:31+09:00
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 미래내일 일경험 IT 백엔드 개발자 면접 후기
  - 미래내일 일경험 IT 백엔드 개발자 면접 후기
  - 파이썬과 자바 언어의 차이
  - 스프링 시큐리티 설명 부탁드립니다
  - 스프링 컨테이너에 대해서 설명해주세요

## 32. [UMC 8기] Spring Boot 파트 서류&면접 합격 후기

- URL: https://velog.io/@jayaione_ele/UMC-8%EA%B8%B0-Spring-%ED%8C%8C%ED%8A%B8-%EC%84%9C%EB%A5%98%EB%A9%B4%EC%A0%91-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2025-03-20
- Rule score: 41
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 스프링과 스프링부트의 차이
  - Node.js와 Spring 경험이 둘 다 있는데, 둘의 장단점 및 차이점
  - 서버 요청이 많을 때 해결 방법
  - API, REST API에 대한 설명
  - Oauth와 자체 로그인의 차이

## 33. 백엔드 중소기업 첫번째 면접 후기

- URL: https://velog.io/@robolab1902/%EB%B0%B1%EC%97%94%EB%93%9C-%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85-%EC%B2%AB%EB%B2%88%EC%A7%B8-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2022-01-19
- Rule score: 40
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 기억 나는 것만 살짝 생각해보면, Framework 중 MVC 모델이 무엇이고 MVC 모델을 쓰는 종류엔 무엇이 있냐
  - AOP와 DI를 설명해보아라
  - JPA의 영속성 컨텍스트가 해주는 역할이 무엇이냐?
  - [Spring] DI가 무엇일까?

## 34. [2024.10 ~ 2024.12] 백엔드 개발 3개월 인턴 회고 (+ 면접 후기)

- URL: https://wooing1084.tistory.com/42
- Source: tistory
- Published: 2025-03-17T15:42:58+09:00
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Git의 통신은 어떻게 동작할까?
  - Git의 통신은 어떻게 동작할까?
  - JPA에 대한 설명

## 35. UMC 5기 합격 후기 (서버 Spring 파트, 울산대학교)

- URL: https://raon-2.tistory.com/33
- Source: tistory
- Published: 2023-09-12T09:37:53+09:00
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 면접 질문 으로는 왜 서버에 지원했는지, JPA, JDBC,MVC 패턴, rest api와 api의 차이 등 에 대해서 여쭤보셨어요
  - 제가 지난 4기 UMC에 웹이었고, 서버에 대한 경험이 없어서 그런지 그에 맞춰서 면접 질문을 내주신 것 같았어요.(개인적인 생각입니다 실제로 그러신게 아님
  - [Github/Git] 깃허브 PR이란?

## 36. JavaScript 신입 백엔드 개발자 기술 면접 후기

- URL: https://velog.io/@s_hajin/JavaScript-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-05-12
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 웹 브라우저에서의 JS와 Node.js의 차이점
  - DB 설계는 어떻게 했는지
  - DB 쿼리문을 작성하기 위해 연결을 어떻게 했는지

## 37. [스타트업 백엔드 일기😕] 경력직 이직 개발자 질문 리스트 정리

- URL: https://velog.io/@jee-9/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%97%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%9D%BC%EA%B8%B0-%EA%B2%BD%EB%A0%A5%EC%A7%81-%EC%9D%B4%EC%A7%81-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%A7%88%EB%AC%B8-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A6%AC
- Source: velog
- Published: 2025-03-05
- Rule score: 39
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Django와 mysql을 함께 사용한 이유는 무엇인가 (Django의 권장사항은 PostgresQL이라고 합니다
  - https와 http의 차이 (아 이건 공개키 이야기를 했어야하는데...단어가 ㅠ
  - 경험을 말하며) 이렇게 대답했고, b-tree 관련해서는 ElasticSearch LIKE 쿼리에서 본 내용들을 토대로, 이런 개념인 것을 이해한다

## 38. 간단한 면접 후기

- URL: https://velog.io/@god0478/%EA%B0%84%EB%8B%A8%ED%95%9C-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2024-10-16
- Rule score: 38
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - redis, elasticCache?
  - 자바스크립트 es6 이란 무엇인가 ?
  - jwt vs session 차이
  - es6 이게 뭔말인지 몰랐던게 자바스크립트 표준 버전이였다 간단하게 const let var 이런거가 어떤 식으로 사용되고 어떻게 활용되는지 에대한 표준 이런거 였는데 이것을 통틀어서 저렇게 말하는지 솔직히 처음알았다

## 39. 비전공자의 백엔드개발자 면접후기

- URL: https://velog.io/@9ruem2/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90%EC%9D%98-%EB%B0%B1%EC%97%94%EB%93%9C%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-12-19
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - api문서화를 하면서 목객체를 사용할 수 있는데 왜 swagger를 사용했나?
  - http메서드에 대해 설명해보라
  - 시큐리티는 api문서화할 때 어떻게 적용했나?
  - mvc패턴은 어떤것을 사용했나?
  - 데이터베이스는 어디수준까지 알고있나?

## 40. 면접 질문 정리 및 후기

- URL: https://velog.io/@god0478/%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC-%EB%B0%8F-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2025-03-11
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 늘있는 n+1 문제 db구조와 엔티티 구조가 다르기 때문에 발생하는 문제 보통 fetch join이나 batsize를 사용해서 한번에 데이터를 긁어와서 해결
  - redis 관련해서 분산락에 대한 질문 reddisson 방식과 lettuce 방식의 차이점
  - 그리고 인증 관련해서 jwt 방식과 session 방식의 차이 그리고 jpa와 hibernate가 뭐고 어떤 차이가있는지 에대한 질문이였습니다
  - 그리고 객체지향을 무엇이고 왜 쓰는지 에대한 질문 등등 엄청 많았는데 여기에 뭐 알고리즘에 대한 이야기등 솔직히 기술 면접이라고 해가지고 뭐 간단한거나 코태 볼줄 알았는데 정의나 개념 관련해서 너무 자세하게 물어보셔서 당황했습니다

## 41. 당근마켓 면접 후기 및 회고

- URL: https://velog.io/@dion/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0-%EB%B0%8F-%ED%9A%8C%EA%B3%A0
- Source: velog
- Published: 2020-11-07
- Rule score: 37
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 당근마켓에서는 알고리즘 문제 말고 실제 문제를 해결할 역량을 갖춘 개발자를 원하는 느낌 을 받았습니다
  - 백기선님 온라인 스터디 1주차 - JVM은 무엇이며 자바 코드는 어떻게 실행하는 것인가
  - velog 메인에서 보고 궁금해서 들어왔는데 Dion 글이었군요 ㅎㅎ 좋은 경험 공유해주셔서 감사합니다

## 42. 프론트엔드 개발자 인터뷰 후기 (면접 질문 정리)

- URL: https://velog.io/@tmmoond8/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B8%ED%84%B0%EB%B7%B0-%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC-%EC%9E%91%EC%84%B1-%EC%A4%91
- Source: velog
- Published: 2018-11-16
- Rule score: 35
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 클라이언트 쪽의 스크립트(예: 자바 스크립트)를 다루는 방식에 차이가 있다
  - '인사이드 자바스크립트' 책과 등 실행컨텍스트를 설명하는 많은 곳에서 기준이 되는 버전은 es3 버전이라고 합니다
  - zerocho님의 Node.js 교과서에 참고 자료로 이벤트 루프에 대한 시각적 설명 링크가 있는데, 이벤트 루프를 이해하기 좋을 것 같습니다
  - < script type = " text/javascript " src = " http://kingbbode.com/result.json?callback=parseResponse " > </ script >

## 43. 현대오토에버 24년 10월 신입채용 1차면접 후기 (백엔드/차량 관제)

- URL: https://xorjsghkd1011.tistory.com/173
- Source: tistory
- Published: 2024-12-04T11:41:54+09:00
- Rule score: 33
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 새 프로젝트에서 MongoDB, Redis 사용 예정 → 둘다 NoSQL인데 차이는?
  - CI/CD 파이프라인 구축 경험 → 거기서 git도 사용해봤는지?
  - git이 파이프라인에서 어떻게 활용되는가?

## 44. 1년차 주니어 프론트 개발자 이직 후기

- URL: https://velog.io/@ohaeseong/1%EB%85%84%EC%B0%A8-%EC%A3%BC%EB%8B%88%EC%96%B4-%ED%94%84%EB%A1%A0%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B4%EC%A7%81-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2021-10-06
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 특이했던 것은 지금 껏 코딩 테스트라고 하면 주로 프로그래머스나 백준과 같은 알고리즘을 이용한 문제 해결을 주로 생각하고 준비 해왔는데 카카오 모빌리티에서는 아예 리액트 컴포넌트를 하나 주고 특정 기능을 만드는 것 처럼 완전히 실무적으로 코딩 테스트가 진행 되었습니다

## 45. [UMC] UMC 9기 Spring Boot 서류 + 면접 합격 후기

- URL: https://velog.io/@gthwynn/UMC-UMC-9%EA%B8%B0-%EC%84%9C%EB%A5%98-%EB%A9%B4%EC%A0%91-%ED%95%A9%EA%B2%A9-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2025-09-19
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Spring Boot 파트를 선택한 이유는 무엇인가요?
  - 아직 경험하지 못한 배포, DB 관리, CI/CD, 메시지 큐 등 실무 기술에 도전하려 함
  - DB 사용 경험이 있는지 or 없다면 2주 만에 어떻게 실전 쿼리 작성법을 익힐 것인지
  - 게시글에 해시태그를 여러 개 달 수 있고, 하나의 해시태그가 여러 게시글에 사용될 때, DB 테이블을 어떻게 설계할 것인지
  - API가 무엇이며, REST API란 무엇인지

## 46. DB그룹 계열사 신입사원들이 직접 밝혔다! 면접 질문 및 합격 팁

- URL: https://www.dbblog.co.kr/842
- Source: www.dbblog.co.kr
- Published: 2017-09-06T16:01:08+09:00
- Rule score: 29
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - “아직도 직접 일 하세요?” DB Inc

## 47. [취준] 백엔드 개발자 신입 첫 면접 후기

- URL: https://velog.io/@seoya_lee/%EC%B7%A8%EC%A4%80-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%8B%A0%EC%9E%85-%EC%B2%AB-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-02-11
- Rule score: 28
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - SQL Injection을 아는지?
  - 포트폴리오에 언급) 쿼리빌더를 제작할 때 어떤 방식으로 했는지?

## 48. [2025년 10월] 토스뱅크 백엔드 개발자 직무면접 후기

- URL: https://velog.io/@eddy159/2025%EB%85%84-10%EC%9B%94-%ED%86%A0%EC%8A%A4%EB%B1%85%ED%81%AC-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%A7%81%EB%AC%B4%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2025-11-02
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - MSA 환경에서의 실무 경험 부족
  - 이번 면접을 준비하고 경험하면서 MSA와 대규모 트래픽 처리 에 대한 관심이 생겼습니다
  - 경험이 부족하다면, 토이 프로젝트라도 MSA 환경으로 구성해보면서 직접 부딪혀보려고 합니다

## 49. 신입 웹 퍼블리셔 인성+기술 면접 후기

- URL: https://velog.io/@kyung_99/%EC%8B%A0%EC%9E%85-%EC%9B%B9-%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94-%EC%9D%B8%EC%84%B1%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2022-08-25
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Q: JQuery랑 JavaScript 차이는 무엇인가?
  - Q: 리액트 서버는 무엇을 쓰는지?
  - [CSS] display 속성 block, inline-block, inline 차이점

## 50. [SoMa] 이제서야 쓰는 SW마에스트로 14기 면접 탈락 후기

- URL: https://velog.io/@win-luck/SoMa-%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4-%EB%A7%88%EC%97%90%EC%8A%A4%ED%8A%B8%EB%A1%9C-14%EA%B8%B0-%EB%A9%B4%EC%A0%91-%ED%83%88%EB%9D%BD-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-07-09
- Rule score: 27
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 보너스 질문) REST API 종류?

## 51. [신입 개발자] 기술 면접 질문 정리

- URL: https://velog.io/@hyeeunism/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0-%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EC%A0%95%EB%A6%AC
- Source: velog
- Published: 2023-04-06
- Rule score: 26
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - DB모델링을 할때 프로시저를 썼는데 프로시저를 쓴 이유는?

## 52. 데브시스터즈 서버 직군은 왜 코딩 면접을 볼까?

- URL: https://tech.devsisters.com/posts/server-position-coding-test/
- Source: tech.devsisters.com
- Published: 2022-06-10
- Rule score: 24
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 데브시스터즈 서버 직군은 왜 코딩 면접을 볼까?
  - 데브시스터즈 서버 직군은 왜 코딩 면접을 볼까?

## 53. 첫 면접 후기

- URL: https://velog.io/@junsu930/%EC%B2%AB-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-07-20
- Rule score: 24
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - spring framework는 사용 가능하지만 spring boot나 전자정부 프레임워크는 사용하지 않았어서 그 차이를 좀 메꿀 수 있게 공부해야 할 것 같다
  - pl/sql이란?
  - 전자정부프레임워크와 spring boot의 차이점

## 54. 데브시스터즈 서버 개발자 면접 후기

- URL: https://velog.io/@suunn001/%EB%8D%B0%EB%B8%8C%EC%8B%9C%EC%8A%A4%ED%84%B0%EC%A6%88-%EC%84%9C%EB%B2%84-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2026-01-06
- Rule score: 23
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 단계 온라인 코딩 테스트 알고리즘 및 문제 해결 능력 평가

## 55. 면접후기 + 질문리스트

- URL: https://velog.io/@sarahsea/%EB%A9%B4%EC%A0%91%ED%9B%84%EA%B8%B0-%EC%A7%88%EB%AC%B8%EB%A6%AC%EC%8A%A4%ED%8A%B8
- Source: velog
- Published: 2022-01-12
- Rule score: 22
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - javascript에서 원시형과 참조형에 대해 설명해달라
  - 주에서 백엔드도 했다던데, 로그인 기능 어떻게 구현했나?

## 56. [스터디] 신입 백엔드 취준생을 위한 모의 면접

- URL: https://velog.io/@leesomyoung/%EC%8A%A4%ED%84%B0%EB%94%94-%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EC%B7%A8%EC%A4%80%EC%83%9D%EC%9D%84-%EC%9C%84%ED%95%9C-%EB%AA%A8%EC%9D%98-%EB%A9%B4%EC%A0%91
- Source: velog
- Published: 2023-06-17
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 면접을 어떻게 준비해야 할 지 모르고, 실전 감각을 기르고 싶은 주니어 백엔드 개발자들에게 많은 도움이 될 것이라고 생각한다

## 57. 스타트업 면접 후기

- URL: https://velog.io/@kimseungho/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%97%85-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2024-11-01
- Rule score: 21
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 테스트와 같은 과정이 실무와 같다면 RDBMS를 설계는 어떻게 진행하는가?

## 58. java 면접 질문 정리 - 1 : 정답 -

- URL: https://velog.io/@hi5004gun/%EB%A9%B4%EC%A0%91-%EC%A7%88%EB%AC%B8-%EA%B4%80%EB%A0%A8-%EC%A0%95%EB%A6%AC-2
- Source: velog
- Published: 2023-12-28
- Rule score: 20
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - java 언어를 창시한 사람은 누구인가?

## 59. 웹 개발자로 면접 후기

- URL: https://velog.io/@developer119/%EC%9B%B9-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A1%9C-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2021-03-18
- Rule score: 19
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 구직중이라 여러 회사에서 면접 제의가 오고 있다, 게임개발을 하면서 간단한 프론트엔드와 백엔드서버를 만저본 경험을 이력서와 포트폴리오에 기재했는데, 그로인해 웹 개발사에서도 면접제의가 온다
  - 싱글페이지 웹가 서버사이드 렌더링의 차이점 및 사용자가 느낄 수 있는 장점 및 단점
  - 자바스크립트는 싱글스레드인데 비동기가 처리 되는 방식에대한 설명

## 60. 중소기업 신입 개발자 면접 후기

- URL: https://velog.io/@yeony402/%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85-%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2024-06-20
- Rule score: 19
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - JWT를 사용한 이유가 무엇인가요?
  - Spring 프레임워크에 대해 설명해보세요
  - 어떤 쿼리문 작성했는지..?

## 61. [취준] 첫 IT직무 면접을 돌아보며

- URL: https://velog.io/@perhona3422/%EC%B7%A8%EC%A4%80-%EC%B2%AB-IT%EC%A7%81%EB%AC%B4-%EB%A9%B4%EC%A0%91%EC%9D%84-%EB%8F%8C%EC%95%84%EB%B3%B4%EB%A9%B0
- Source: velog
- Published: 2022-08-04
- Rule score: 18
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Spring AOP에 대해 설명해보세요
  - 값을 불러오는 방법에는 'Call by value'와 'Call by reference'가 있는데, Java는 어떤 방식인지 설명해보세요

## 62. 신입 백엔드 개발자 취뽀여정 1탄 - 중소(si)기업 면접 후기

- URL: https://velog.io/@kimhyejin67/%EC%8B%A0%EC%9E%85-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EB%BD%80%EC%97%AC%EC%A0%95-2%ED%83%84-%EC%A4%91%EC%86%8Csi%EA%B8%B0%EC%97%85-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2024-02-03
- Rule score: 17
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - SQL문 얼마나 잘 쓸 줄 아는지?

## 63. 인생 첫 개발 면접 1트에 성공한 후기 (웹 개발 인턴 합격 수기)

- URL: https://velog.io/@osohyun0224/%EC%9D%B8%EC%83%9D-%EC%B2%AB-%EA%B0%9C%EB%B0%9C-%EB%A9%B4%EC%A0%91-1%ED%8A%B8%EC%97%90-%EC%84%B1%EA%B3%B5%ED%95%B4%EB%B3%B4%EA%B8%B0-%EC%9B%B9-%EA%B0%9C%EB%B0%9C-%EC%9D%B8%ED%84%B4-%ED%95%A9%EA%B2%A9-%EC%88%98%EA%B8%B0
- Source: velog
- Published: 2023-12-25
- Rule score: 15
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 개발자 인생을 놓고 보았을 때 저년차에는 프론트 뿐만아니라 백엔드 다 경험해봐야한다고 생각해 이 회사에 지원했고 아직 한달 뿐이지만 많은 기술을 실무에서 배웠습니다

## 64. 웹퍼블리셔 면접 후기

- URL: https://velog.io/@wizwic/%EC%9B%B9%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2022-09-27
- Rule score: 15
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - Javascript와 jQuery 얼마나 다룰 줄 아세요?

## 65. 2022년 하반기 (주)DB하이텍 면접후기 | 41,046 번째 면접경험 - 사람인

- URL: https://www.saramin.co.kr/zf_user/interview-review/detail/idx/41046/%28%EC%A3%BC%29DB%ED%95%98%EC%9D%B4%ED%85%8D-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: saramin
- Published: 2024-07-23
- Rule score: 14
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 년 하반기 (주)DB하이텍 면접후기 | 41,046 번째 면접경험 - 사람인 - 사람인
  - 면접 경험 공유 (주)DB하이텍

## 66. 준비가 정말정말 미흡했던 통화 기술면접 후기;

- URL: https://velog.io/@terria1020/%EC%A4%80%EB%B9%84%EA%B0%80-%EC%A0%95%EB%A7%90%EC%A0%95%EB%A7%90-%EB%AF%B8%ED%9D%A1%ED%96%88%EB%8D%98-%ED%86%B5%ED%99%94-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2023-06-22
- Rule score: 14
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - HTTP 1.0 vs HTTP 2.0 차이
  - 이 중에서 아는 내용(JVM, HTTP, ORM, 인터페이스 vs 추상클래스 차이, 인터프리터 언어 vs 컴파일 언어 차이) 에 대해서는 답변을 했긴 했으나 정말 너무 어리바리하게 대답했고, 모르는 것에 대해서는 패스한 것도 있고 정말 엉망진창으로 면접을 진행했다

## 67. 지마켓 백엔드 면접 후기

- URL: https://velog.io/@guswlsapdlf/%EC%A7%80%EB%A7%88%EC%BC%93-%EA%B8%80%EB%A1%9C%EB%B2%8C-%EB%B0%B1%EC%97%94%EB%93%9C-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0
- Source: velog
- Published: 2022-09-16
- Rule score: 11
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 자기 소개 과정에서 github에 public repository에 올려 둔 프로젝트가 있다고 언급했었는데 그 github을 보시고 "이 코드를 이렇게 작성한 이유가 무엇인지?"라는 질문을 받았었다

## 68. 나의 첫 개발회사 면접 후기(바로고 인턴 면접)

- URL: https://velog.io/@klqwrx7004/%EB%82%98%EC%9D%98-%EC%B2%AB-%EA%B0%9C%EB%B0%9C%ED%9A%8C%EC%82%AC-%EB%A9%B4%EC%A0%91-%ED%9B%84%EA%B8%B0%EB%B0%94%EB%A1%9C%EA%B3%A0-%EC%9D%B8%ED%84%B4-%EB%A9%B4%EC%A0%91
- Source: velog
- Published: 2022-03-30
- Rule score: 11
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 파이썬과 자바스크립트를 둘다 해보면서 느꼈던 차이점은 무엇인지?
  - 자바스크립트를 하면서 async/await을 활용하였다고 하였는데 이 async/await을 왜 쓰는건지?
  - 마지막으로 공통질문을 하셨는데 Rest API 에 대해 자유롭게 설명해보시라고 하셨다

## 69. 신입 개발자 취업 후기 (면접팁)

- URL: https://velog.io/@krhopy/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%B7%A8%EC%97%85-%ED%9B%84%EA%B8%B0-%EB%A9%B4%EC%A0%91%ED%8C%81
- Source: velog
- Published: 2023-01-16
- Rule score: 10
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - python과 java의 차이점 ( 둘다 공부를 했어서 질문이 들어왔어용
  - svn 과 github 차이 ( 둘다 써봤어서 물어보심

## 70. 2021 가비아 백엔드 개발자 면접까지 후기

- URL: https://kkyu67.tistory.com/entry/2021-%EA%B0%80%EB%B9%84%EC%95%84-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EB%A9%B4%EC%A0%91%EA%B9%8C%EC%A7%80-%ED%9B%84%EA%B8%B0
- Source: tistory
- Published: 2022-01-04T09:23:25+09:00
- Rule score: 9
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 백엔드에 병특 경험이 어떻게 도움이 될 수 있는지

## 71. [Java] 첫 면접 스터디 후기 & 질문 모음

- URL: https://velog.io/@nhe0622/Java-%EC%B2%AB-%EB%A9%B4%EC%A0%91-%EC%8A%A4%ED%84%B0%EB%94%94-%ED%9B%84%EA%B8%B0-%EC%A7%88%EB%AC%B8-%EB%AA%A8%EC%9D%8C
- Source: velog
- Published: 2024-12-02
- Rule score: 8
- Rule reason: 실제 면접 신호와 구체 백엔드 기술 질문 후보가 있음
- Rule question samples:
  - 가비지 컬렉션이 어떻게 작동하는지와 그 알고리즘에 대해서 설명하세요
  - Java가 컴파일되는 과정에 대해 설명하세요
  - 자바의 주요 특징에 대해 설명하세요
