# Java 1단계: 단위 테스트

## 학습 목표
하나의 Account 객체가 정상·경계·예외 입력을 정확히 처리하는지 검증합니다.

## 구현과 테스트 코드
`src/main/java/edu/testing/Account.java` → `src/test/java/edu/testing/AccountTest.java`

## 테스트 케이스
잔액 1,000원에서 400원 출금 → 600원; 1,000원 전액 출금 → 0원; 1,001원 출금 거부; 0원·음수 출금 거부.

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
Repository나 Service 없이 개별 Account 기능만 검증합니다.
