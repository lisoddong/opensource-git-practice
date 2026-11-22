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
