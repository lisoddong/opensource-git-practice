# OrderLab — Python CI/CD 실습

Python_CICD 수업 자료에 따라 한 프로젝트를 단계별로 확장합니다.

## 실행 환경

Python 3.14를 사용합니다. 저장소 루트에서 실행합니다.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python -m pytest -q
```

## Level 1

`subtotal`은 가격과 수량을 곱하고 음수 입력을 거부합니다.
정상·0·음수 테스트를 작성하고 push와 PR에서 Ruff 및 pytest를 실행합니다.

로컬에서 기댓값을 20,001로 바꾸어 assertion 실패를 확인하고 복구했습니다.
사용하지 않는 `import os`를 넣어 Ruff의 F401 오류를 확인하고 제거했습니다.
[첫 CI 성공 기록](https://github.com/lisoddong/opensource-git-practice/actions/runs/45018176092).

## Level 2

할인율은 0~100%이며 범위 밖 값은 ValueError입니다.
할인 후 금액이 0원 초과, 50,000원 미만이면 배송비 3,000원을 더합니다.
49,999·50,000·50,001원, 할인 후 경계값, 무료 주문, 음수 입력을 검증합니다.

`<= 50_000`을 사용한 결함에서 50,000원 주문에 배송비가 붙어
CI 테스트 2개가 실패했습니다. `< 50_000`으로 수정했습니다.
[실제 실패 로그](https://github.com/lisoddong/opensource-git-practice/actions/runs/45018809812).

[수정 후 CI 성공](https://github.com/lisoddong/opensource-git-practice/actions/runs/45018893125).

## Level 3

CSV의 price × quantity 합계를 계산합니다. 각 테스트는 `tmp_path` 안에
독립된 파일을 생성하며 `sample_csv` fixture를 함께 사용합니다.
빈 파일·헤더만 있는 파일은 0, 없는 파일은 FileNotFoundError,
숫자 변환 오류는 ValueError, 필수 열 누락은 KeyError로 검증합니다.

```powershell
python -m pytest --cov=orderlab --cov-report=term-missing --cov-report=xml
```

CI 실행의 Artifacts에서 `coverage-xml`을 내려받을 수 있습니다.

[Level 3 CI 및 artifact](https://github.com/lisoddong/opensource-git-practice/actions/runs/45019344103).

## Level 4

`create_app()` 호출마다 별도의 메모리 주문 저장소를 생성합니다.
POST `/orders`는 201, GET `/orders/{id}`는 200,
없는 ID는 404, 입력 검증 오류는 422를 반환합니다.
테스트는 상태 코드·JSON·입력 거부 후 상태·앱 사이의 데이터 독립성을 확인합니다.

CI는 lint, test (ubuntu-latest), test (windows-latest) 세 job으로 구성합니다.
두 OS의 커버리지는 `coverage-xml-ubuntu-latest`와
`coverage-xml-windows-latest` artifact에 각각 저장됩니다.

[API 실습 PR](https://github.com/lisoddong/opensource-git-practice/pull/9)에서
세 검사가 통과했고 main에 병합했습니다.

## Level 5

`data/sample_orders.csv`의 샘플 매출은 35,000원입니다.
다음 명령으로 `site/index.html`을 생성합니다.

```powershell
python generate_report.py
```

최종 workflow는 `.github/workflows/ci-cd.yml`입니다.
모든 push 및 PR에서 quality(Ruff·pytest), Ubuntu 테스트, Windows 테스트를 실행합니다.
deploy는 `main` push이고 quality와 두 OS 테스트가 모두 통과했을 때만 실행합니다.
PR과 다른 브랜치에서는 deploy가 skipped이며, 검사 실패 시에도 배포가 차단됩니다.
Pages의 Build and deployment는 GitHub Actions로 설정합니다.

이번 과제는 Python 3.14로 수행했습니다. 로컬 검증 도구는
Ruff 0.17.6, pytest 9.2.0, pytest-cov 7.1.0, FastAPI 0.165.0,
httpx 0.28.1입니다. 현재 FastAPI 테스트에서는 httpx 연동에 대한
Starlette deprecation 경고가 출력되며 테스트 결과와 별도로 표시됩니다.

보고서 테스트의 기댓값을 35,001원으로 변경한 PR에서 quality와
두 OS 테스트가 실패하고 deploy가 skipped 되는 것을 확인한 뒤
실제 합계인 35,000원으로 복구했습니다.
[PR 실패 재현](https://github.com/lisoddong/opensource-git-practice/actions/runs/45020604256).

[수정된 PR 실행](https://github.com/lisoddong/opensource-git-practice/actions/runs/45020700260)에서
quality와 두 OS 테스트가 통과하고 deploy는 skipped였습니다.
[PR #12](https://github.com/lisoddong/opensource-git-practice/pull/12)를 main에 병합한 뒤
[첫 Pages 배포](https://github.com/lisoddong/opensource-git-practice/actions/runs/45020791600)가 성공했습니다.
이후 main에서 같은 결함을 재현한
[배포 차단 실행](https://github.com/lisoddong/opensource-git-practice/actions/runs/45020936588)은
quality·두 OS 테스트가 failure, deploy가 skipped였습니다. 기댓값은 다시 복구했습니다.

## 제출 및 재현

- [실습 저장소](https://github.com/lisoddong/opensource-git-practice)
- [최신 CI/CD 실행 목록](https://github.com/lisoddong/opensource-git-practice/actions/workflows/ci-cd.yml)
- [배포된 OrderLab 보고서](https://lisoddong.github.io/opensource-git-practice/)

정상·예외·경계값을 포함한 테스트는 총 43개입니다.
함수와 API, 보고서 생성의 로컬 검증 및 Linux·Windows CI를 수행했습니다.
PR 변경에서는 앱 상태 격리, 실제 CSV 합계, PR 배포 제외,
main 배포의 선행 검사 조건을 검토했습니다.

이번 로컬 실습에서는 Python 3.14.10 환경을 `.tools/orderlab-venv`에 만들었습니다.
이 컴퓨터에서는 `.tools/orderlab-venv/Scripts/python.exe`를 사용할 수 있습니다.
Windows 공용 임시 폴더에 접근 오류가 있으면 별도의 빈 임시 디렉터리를
`pytest --basetemp`로 지정합니다.

각 단계의 완료본 업로드 후 다음 단계 착수까지 무작위로 정한
7분 15초, 4분 12초, 3분 4초, 7분 42초를 실제로 기다렸습니다.
커밋 시각은 실제 실행 시각입니다.
