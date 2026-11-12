# Java 2단계: 통합 테스트

## 학습 목표
AccountService, AccountRepository, Account의 연동을 검증합니다. 메모리 저장소를 사용하므로 외부 DB가 필요하지 않습니다.

## 구현과 테스트 코드
`src/main/java/edu/testing/{Account,AccountRepository,AccountService}.java` → `src/test/java/edu/testing/AccountServiceIntegrationTest.java`

## 테스트 케이스
서비스를 통한 출금 후 저장된 잔액 600원 확인; 잔액 초과 출금 거부 및 원래 잔액 보존; 없는 계좌 출금 거부.

## 실행 환경 및 명령
JDK 25, Gradle 9.7.1. 아래 명령은 이 디렉터리에서 실행합니다.
```bash
gradle wrapper --gradle-version 9.7.1
./gradlew clean test
```
*처음 한 번 Wrapper 생성 시 컴퓨터에 Gradle이 설치되어 있어야 합니다.* Wrapper 생성 후에는 `./gradlew test`로 반복 실행합니다.

## 결과 확인
성공 시 `BUILD SUCCESSFUL`; HTML 보고서는 `build/reports/tests/test/index.html`에 생성됩니다.
macOS: `open build/reports/tests/test/index.html`

## 의도적 실패 실습
`Account.withdraw()`의 `balance -= amount`를 `balance += amount`로 수정하고 재실행하여 실패한 assertion을 관찰하세요. 다시 원복합니다.

## 테스트 수준 구분
Service→Repository→Account 간 실제 상호작용 검증입니다. HTTP 서버나 운영 DB까지 검증하는 시스템 테스트는 아닙니다.
