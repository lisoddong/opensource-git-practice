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
