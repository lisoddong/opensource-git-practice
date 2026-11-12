# 오픈소스 깃 연습 — 실제 실행 결과

실행일: 2026-11-12 (Asia/Seoul). 저장소: https://github.com/lisoddong/opensource-git-practice

## 로컬 테스트

환경: Windows, Python 3.13.14 / pytest 9.2.0, Temurin JDK 25.0.5 / Gradle 9.7.1.

| 실습 | 정상 | 의도적 결함 후 | 원복 후 |
|---|---|---|---|
| Python 단위 | 5 통과 | 2 실패·3 통과 | 5 통과 |
| Python 통합 | 3 통과 | 1 실패·2 통과 | 3 통과 |
| Java 단위 | 4 통과 | 2 실패·2 통과 | 4 통과 |
| Java 통합 | 3 통과 | 1 실패·2 통과 | 3 통과 |

결함: 출금의 `balance -= amount`를 `balance += amount`로 바꿈.
예: 1,000원에서 400원 출금 시 예상 600원, 결함 결과 1,400원.
실습 후 코드 원복 완료. 로그와 XML은 이 폴더에 있으며 로컬 사용자 경로·PC 이름은 제거했습니다.
Java 테스트는 성공했지만 Gradle 10 호환성 관련 deprecation 경고가 있습니다.

## GitHub Actions

아래 25종을 모두 실제 실행했습니다. `failure`와 `skipped`를 성공으로 바꾸지 않았습니다.

| 파일 | 실제 결과 | 실행 기록 |
|---|---|---|
| condition-workflow.yaml | skipped | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174167909) |
| condition.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174104700) |
| expected-workflow-error.yaml | failure | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174240443) |
| expected-yaml-error.yaml | failure | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174340961) |
| first-context.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174342484) |
| first-env_ref.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174171808) |
| first-env.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174176066) |
| first-hello.yml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174342462) |
| first-inter_env_ref.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174180435) |
| first-manual.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174184868) |
| first-run_time_error.yaml | failure | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174188904) |
| first-secret_ref.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174240705) |
| first-shell.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174193010) |
| first-val_ref.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174197327) |
| hash.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174201392) |
| job-status.yaml | failure | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174205462) |
| json-function.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174209861) |
| literal.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174214224) |
| object-filter.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174219309) |
| operator.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174224579) |
| run-name.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174228752) |
| status-check.yaml | failure | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174233365) |
| string-create.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174237847) |
| string-function.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174242210) |
| var.yaml | success | [실행 보기](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174247009) |

### 예상된 실패 및 건너뛰기

- run_time_error: 0으로 나누기에서 실패하여 뒤의 기본 조건 step은 실행되지 않습니다.
- job-status: job1 실패, job2 건너뛰기, failure 조건 job3 및 always 조건 job4 성공.
- status-check: Fail Step 실패 후 failure/always 단계는 실행됩니다. 전체 결론은 failure입니다.
- condition-workflow: actor가 guest가 아니어서 job1 및 이를 필요로 하는 job2/job3을 건너뜁니다.
- workflow_error: jobs/runs-on 대신 job/run-on을 사용한 원본의 정의 오류로 job 실행 전에 실패합니다.
- yaml_error 원본은 유효한 YAML이라 [원본 실행은 성공](https://github.com/lisoddong/opensource-git-practice/actions/runs/43174231768)했습니다. 별도 오류 브랜치에서 `runs-on: [ubuntu-latest`로 닫는 대괄호를 누락시켜 실제 문법 오류를 관찰했습니다. 원본 보관본은 수정하지 않았습니다.

### 설정·보완 사항

- 1st 하위 예제는 실행용 사본을 workflows 직속에 배치했습니다.
- USERNAME 변수에는 lisoddong을 설정했습니다.
- PASSWORD secret에는 실습용 더미 값만 설정했습니다. 원본의 분할 출력은 마스킹 우회이므로 실행용 사본에서는 전체 마스킹 출력 및 설정 여부 확인으로 대체했습니다.
- env_ref는 Python 단위·통합 프로젝트를 각기 실행합니다.
- 추가 오류 브랜치는 병합하지 않았습니다. 기본 제출 브랜치는 codex/opensource-git-practice입니다.
- 원본의 다른 두 브랜치도 examples/other-branches에 보관했습니다. calculator.py는 numpy import 한 줄이며 numpy 설치 후 정상 실행했습니다. 계산기 기능 구현은 원본에 존재하지 않습니다.
- 최초 pytest 실행에는 PowerShell 인자 전달 오류가 있었으며 수정 후 위 결과를 확인했습니다. 수동 workflow 등록 전의 404도 기본 브랜치 갱신 후 해결했습니다.

총괄: 로컬 정상 테스트 15개 통과, 결함 탐지 6개 실패 확인, 원복 후 15개 통과. Actions 25종의 최종 관찰 결과는 성공 19·예상 실패 5·조건부 건너뛰기 1입니다.
