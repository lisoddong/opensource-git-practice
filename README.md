# 오픈소스 깃 연습

원본: https://github.com/DBChoi85/git-practice

교수님 예제를 내려받아 실행하고 결과를 기록하는 실습 저장소입니다.
기존 원본 커밋의 작성자와 이력을 유지합니다.

- Actions 원본: main, 06d4c2ced3f054a4183f314de5fa6ba904271a88
- Java/Python 원본: feat/testing-unit-integration-labs, 9ff80ffd8f1ab3f60d9413eddd41599a9725ccc1
- 원본 YAML 보관: examples/original-workflows/
- 실행용 YAML: .github/workflows/ (1st 예제를 실행 가능한 직속 경로에 복사)
- Java/Python: 각 프로젝트의 README.md 참고
- 실행 결과: evidence/RESULTS.md (검증 후 작성)

## 실행 시 보완

env_ref의 pytest는 서로 독립된 Python 실습 디렉터리를 각각 실행합니다.
secret_ref에는 실습용 더미 값만 설정하고, 마스킹을 우회하는 분할 출력은 실행하지 않습니다.
문법 오류 예제 2개는 별도 오류 실습 브랜치에서 검증합니다.
런타임 오류 및 상태 함수 예제의 실패는 관찰 대상이며 정상 코드로 숨기지 않습니다.

GitHub Actions는 로컬 PC에서 파일을 준비하고 GitHub 러너에서 실행합니다.
Java/Python 테스트는 로컬 실행 결과와 의도적 결함 삽입 후 결과를 구분합니다.

## Windows에서 다시 실행

현재 PC에는 `.venv`와 `.tools`에 실습 도구가 준비되어 있습니다.
```powershell
.\run-local-tests.ps1 -IncludeJava
```
다른 PC에서는 Python 3.12 이상 및 JDK 25를 설치하고 각 실습 README를 따릅니다.
Python 프로젝트는 같은 이름의 bank.py를 각각 가지므로 pytest를 디렉터리별로 따로 실행합니다.
Java Wrapper는 포함되어 있으므로 각 Java 실습 폴더에서 `.\gradlew.bat clean test`를 실행할 수 있습니다.

## 관찰할 점

- 단위 테스트는 Account만, 통합 테스트는 Service → Repository → Account 연결을 검증합니다.
- 출금의 `-=`를 `+=`로 바꾸면 정상/전액 출금 테스트가 잔액 오류를 찾아냅니다.
- Actions env는 workflow/job/step 범위에 따라 보이는 값이 다릅니다.
- success/failure/always와 needs는 실패 이후 실행할 step/job을 결정합니다.
- 조건부 예제의 guest 조건은 lisoddong 실행에서 거짓이므로 job이 skipped 됩니다.
- 원본 yaml_error.yaml은 실제 유효한 YAML입니다. 원본 성공과 추가 문법 결함 실패를 모두 기록합니다.
- test 브랜치의 calculator.py는 numpy import 한 줄뿐입니다. 사칙연산 구현은 원본에 없습니다.

실행·환경 준비와 결과 정리는 Codex의 도움을 받아 수행했습니다. 교수님 원본 코드와 실제 결과를 바탕으로 작성했습니다.
