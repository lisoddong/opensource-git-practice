# Python 2단계: 통합 테스트

## 학습 목표
Service, Repository, Account의 상호작용을 검증합니다. 외부 데이터베이스는 필요하지 않습니다.

## 구현 코드 → 테스트 코드
`bank.py`와 `service.py` → `test_service.py`

## 테스트 케이스
출금 후 잔액 반영, 실패 시 저장 상태 보존, 존재하지 않는 계좌 처리.

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
Service→Repository→Account 연동 검증으로, 전체 서버에 대한 시스템 테스트와는 다릅니다.
