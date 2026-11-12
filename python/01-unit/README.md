# Python 1단계: 단위 테스트

## 학습 목표
Account 객체의 출금 규칙을 독립적으로 검증합니다.

## 구현 코드 → 테스트 코드
`bank.py` → `test_bank.py`

## 테스트 케이스
정상 출금, 잔액 전액 출금, 잔액 초과 거부, 0원/음수 출금 거부.

## 실행
Python 3.12 이상 권장. 이 디렉터리에서 실행합니다.
```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## 결과 확인
터미널의 PASSED/FAILED 및 실패 시 Assertion traceback을 확인합니다. XML 보고서:
```bash
python -m pytest --junitxml=results.xml
```

## 실패 실습
`bank.py`에서 `self.balance -= amount`를 `self.balance += amount`로 바꾸고 실패 결과를 확인한 뒤 복구합니다.

## 테스트 수준 구분
Account 객체의 동작만 검증합니다.
