# 오픈소스 SW 개발 실습

- [1주차](1주차/1st) — GitHub Actions 기초 예제
- [2주차](2주차) — 조건·함수·job 출력·이슈 댓글 및 push 시 이슈 생성
- [3주차 Python CI/CD](3주차/orderlab-project) — OrderLab 계산·CSV·API·Pages 배포
- [3주차 Python 단위 테스트](3주차/python/01-unit) — 은행 계좌 출금 규칙
- [3주차 Python 통합 테스트](3주차/python/02-integration) — 서비스·저장소·계좌 연동

은행 계좌 예제는 [교수님 실습 브랜치](https://github.com/DBChoi85/git-practice/tree/feat/testing-unit-integration-labs/python)의 코드를 복원했습니다.
각 Python 프로젝트 폴더에서 README에 따라 테스트를 실행합니다.
CI는 OrderLab 43개와 은행 계좌 8개 테스트를 Linux·Windows에서 실행합니다.

실행용 워크플로는 GitHub Actions가 인식하는 `.github/workflows`에 있습니다.
[CI/CD 실행 기록](https://github.com/lisoddong/opensource-git-practice/actions/workflows/ci-cd.yml) ·
[배포된 보고서](https://lisoddong.github.io/opensource-git-practice/)
