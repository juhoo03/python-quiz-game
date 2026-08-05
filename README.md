# ⚡ 전기 상식 퀴즈 게임 (Python CLI)

터미널 환경에서 즐기는 파이썬 기반의 객체지향 전기 상식 퀴즈 게임 프로젝트입니다.

---

## 1. 프로젝트 개요 및 주제 선정 이유
- **프로젝트 개요**: 객체지향 프로그래밍(OOP) 개념과 JSON 파일 입출력을 활용하여 개발한 콘솔 기반 퀴즈 프로그램입니다.
- **주제 선정 이유**: 일상생활 및 학문적으로 기초가 되는 '전기 및 회로 기초 지식'을 재미있게 복습하고 상식을 점검할 수 있도록 전기 상식 퀴즈를 주제로 선정했습니다.

---

## 2. 주요 기능 목록
- **📝 퀴즈 풀기**: 저장된 전기 퀴즈를 풀고 100점 만점 기준 점수 산출
- **📌 퀴즈 추가**: 사용자가 문제, 4개 선택지, 정답 번호를 직접 새로 등록 및 저장
- **📋 퀴즈 목록 조회**: 현재 저장된 전체 전기 퀴즈 문제 목록 확인
- **🏆 최고 점수 확인**: 역대 달성한 최고 점수 기록 유지 및 조회
- **🗑️ 퀴즈 삭제 (보너스 기능)**: 목록에서 삭제할 퀴즈 번호를 선택하여 삭제 및 실시간 파일 반영
- **💾 데이터 영속성 (`state.json`)**: 게임을 종료하거나 재실행해도 `state.json`에 최신 데이터 자동 저장/복원
- **🛡️ 예외 처리 및 안정성**: 잘못된 숫자/문자 입력 방지, `Ctrl+C` 및 `EOFError` 강제 종료 시 안전한 자동 저장 처리

---

## 3. 프로그램 실행 방법

```bash
# 프로그램 실행
git clone https://github.com/juhoo03/python-quiz-game.git
cd python-quiz-game
python3 main.py

4. 파일 및 디렉터리 구조
main.py: 메인 메뉴, 사용자 입출력, 메뉴 분기 및 예외 처리

game.py: QuizGame 클래스 (데이터 파일 저장/불러오기, 퀴즈 삭제 등 전체 데이터 관리)

quiz.py: Quiz 클래스 (개별 퀴즈 정보 구성, 출력, 정답 검증 및 직렬화)

state.json: 퀴즈 목록과 최고 점수를 영구 보관하는 UTF-8 인코딩 데이터 파일

.gitignore: Git 추적에서 제외할 파일 설정

5. 데이터 구조 (state.json)
state.json은 루트 디렉터리에 위치하며 UTF-8 인코딩을 지원합니다.

JSON
{
  "quizzes": [
    {
      "question": "전압, 전류, 저항 사이의 관계를 나타내는 법칙은?",
      "choices": [
        "옴의 법칙",
        "패러데이 법칙",
        "키르히호프 법칙",
        "쿨롱의 법칙"
      ],
      "answer": 1
    }
  ],
  "best_score": 100
}
6. Git 커밋 규칙 및 브랜치 전략
커밋 메시지 컨벤션: Feat:, Docs:, Fix:, Refactor: 등의 태그를 활용하여 기능 단위 커밋 실행

브랜치 활용: 기능 구현을 위해 추가 브랜치를 생성하여 작업 후 main 브랜치로 병합(merge) 진행

Git 필수 명령어 7종 사용: init, add, commit, push, pull, checkout, clone 모두 수행 및 검증 완료

7. 새로운 환경에서 설치 및 실행 방법
저장소 복제 (Clone)

Bash
git clone [https://github.com/juhoo03/python-quiz-game.git](https://github.com/juhoo03/python-quiz-game.git)
cd python-quiz-game
프로그램 실행

Bash
python3 main.py
8. 💡 학습한 핵심 개념 및 기술 요약
🐍 Python 기초 & 객체지향 (OOP)
자료형 및 제어문: int, str, list, dict 활용, if/elif/else 분기 처리 및 for, while 반복문 제어

예외 처리 (Exception Handling): try/except를 사용해 ValueError, KeyboardInterrupt(Ctrl+C), EOFError 시 비정상 종료 없이 안전 저장 및 종료 구현

클래스 설계:

Quiz: 개별 퀴즈의 속성(문제, 선택지, 정답)과 정답 검증, JSON 직렬화(to_dict) 담당

QuizGame: 퀴즈 리스트 및 최고 점수 관리, 파일 입출력(save_data, load_data), 삭제 로직 담당

📂 파일 입출력 & 데이터 영속성
JSON handling: json.dump(), json.load()를 활용해 메모리의 객체 상태를 state.json 파일에 저장하고 자동 복원

인코딩 설정: 한글 깨짐 방지를 위해 encoding="utf-8", ensure_ascii=False 옵션 적용

🐙 Git & GitHub 협업 워크플로우
원격 저장소 동기화: 별도 디렉터리 clone 후 수정 사항 push, 기존 디렉터리에서 git pull로 동기화 실습 완료