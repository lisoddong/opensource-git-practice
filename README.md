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
