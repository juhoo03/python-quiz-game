# ⚡ 전기 상식 퀴즈 게임 - Python CLI

> 터미널 환경에서 즐기는 파이썬 기반 객체지향 전기 상식 퀴즈 게임입니다.  
> **OOP, JSON 영속성, Atomic Write, 입력 검증, 예외 처리**를 반영한 콘솔 프로젝트입니다.

---

## 목차

- [1. 프로젝트 개요](#1-프로젝트-개요)
- [2. 주제 선정 이유](#2-주제-선정-이유)
- [3. 개발 환경](#3-개발-환경)
- [4. 주요 기능](#4-주요-기능)
- [5. 모듈 호출 흐름](#5-모듈-호출-흐름)
- [6. 실행 방법](#6-실행-방법)
- [7. 클래스 및 구조 설계](#7-클래스-및-구조-설계)
- [8. 데이터 파일 명세](#8-데이터-파일-명세)
- [9. 파일 저장 정책](#9-파일-저장-정책)
- [10. 대량 데이터 확장성 분석](#10-대량-데이터-확장성-분석)
- [11. Git 규칙 및 실행 증빙](#11-git-규칙-및-실행-증빙)
- [12. 새로운 환경에서 설치 및 실행](#12-새로운-환경에서-설치-및-실행)

---

## 1. 프로젝트 개요

**전기 상식 퀴즈 게임**은 객체지향 프로그래밍과 JSON 파일 입출력을 활용하여 만든 콘솔 기반 퀴즈 프로그램입니다.

사용자는 터미널에서 전기 및 회로 기초 지식과 관련된 문제를 풀 수 있으며, 직접 퀴즈를 추가하거나 삭제할 수 있습니다.

---

## 2. 주제 선정 이유

전기와 회로 기초 지식은 일상생활뿐 아니라 공학 및 과학 학습에서도 중요한 기본 개념입니다.

따라서 사용자가 재미있게 전기 상식을 복습하고 자신의 이해도를 점검할 수 있도록 **전기 상식 퀴즈**를 주제로 선정했습니다.

---

## 3. 개발 환경

### OS 정보
- OS: macOS (버전 15.7.4)
- Shell: zsh (`/bin/zsh`)
- Terminal: macOS 기본 터미널

### Docker & Python 환경
- Docker Engine: 28.5.2 (OrbStack 환경)
- Python Version: Python 3.10 이상
- 외부 라이브러리 없이 Python 표준 라이브러리(`json`, `os`, `sys`, `random`, `datetime`)만 사용

---

## 4. 주요 기능

| 기능 | 설명 |
|---|---|
| 📝 퀴즈 풀기 | 저장된 전기 퀴즈를 풀고 100점 만점 기준 점수 산출 (랜덤 출제, 힌트 지원) |
| 📌 퀴즈 추가 | 사용자가 문제, 4개 선택지, 정답 번호, 힌트를 직접 등록 |
| 📋 퀴즈 목록 조회 | 현재 저장된 전체 퀴즈 문제 목록 확인 |
| 🏆 점수 및 히스토리 | 역대 최고 점수 및 최근 게임 진행 일시/점수 기록 조회 |
| 🗑️ 퀴즈 삭제 | 목록에서 삭제할 퀴즈 번호를 선택하여 삭제 |
| 💾 데이터 영속성 | 프로그램 종료 후에도 `state.json`에 데이터 저장 |
| 🛡️ 예외 처리 | 잘못된 입력(공백/문자/범위 밖), `Ctrl+C`, `EOFError` 상황 처리 |
| 🔄 Atomic Write | 임시 파일 저장 후 `os.replace()`로 안전하게 교체 |

---

## 5. 모듈 호출 흐름

User / CLI Input│▼main.py  ──────── 메뉴 선택 및 입력 검증 ────────► input_helper.py│├── 1. play_quiz()│        └──► Quiz.is_correct()│        └──► score_calculator│├── 2. add_quiz()│        └──► Quiz 객체 생성│        └──► QuizGame.quizzes.append()│├── 3. show_quizzes()│        └──► QuizGame.quizzes 조회│├── 4. show_score()│        └──► QuizGame.best_score & history 조회│└── 5. delete_quiz()└──► QuizGame.delete_quiz()│▼QuizGame.save_data()│▼state.json.tmp│▼os.replace()│▼state.json
> 💡 **모듈 호출 흐름 및 데이터 처리 핵심 요약**
> 
> 1. **입력 검증 (`input_helper.py`)**: 사용자 입력을 받으면 먼저 공백 제거, 정수 변환, 메뉴 허용 범위 검증을 수행하여 비정상 입력을 사전 차단합니다.
> 2. **객체 연산 (`Quiz` & `QuizGame`)**: 메뉴 선택에 따라 퀴즈 풀기(`play_quiz`), 추가(`add_quiz_flow`), 삭제(`delete_quiz_flow`) 등의 로직을 수행하고, `Quiz` 인스턴스 단위로 정답 비교 및 리스트를 제어합니다.
> 3. **원자적 저장 (`Atomic Write`)**: 데이터 변경 발생 시 `QuizGame.save_data()`가 실행되어 `state.json.tmp`에 먼저 안전하게 기록한 뒤 `os.replace()`를 통해 `state.json`으로 교체합니다.

---

## 6. 실행 방법

프로젝트 폴더에서 아래 명령어를 실행합니다.

```bash
python3 main.py
별도의 외부 라이브러리 설치 없이 Python 3 기본 표준 라이브러리만으로 즉시 실행할 수 있습니다.7. 클래스 및 구조 설계OOP 적용 이유1. 캡슐화 및 상태 관리Quiz 클래스는 문제, 선택지, 정답, 힌트 데이터를 하나의 객체로 묶어 관리합니다. is_correct() 메서드를 통해 정답 검증 로직을 객체 내부에서 처리하므로 데이터와 기능이 자연스럽게 결합됩니다.2. 책임 분리와 유지보수성Quiz: 개별 문제의 데이터 표현 및 정답 확인 책임QuizGame: 퀴즈 목록 관리, 최고 점수/히스토리 갱신, JSON 파일 입출력 책임input_helper: 사용자 콘솔 입력 유효성 검증 책임3. 요구사항 변경 시 수정 가이드요구사항 변경 시나리오수정 대상 파일/클래스/메서드정답 채점 방식 / 점수 계산 변경game.py의 QuizGame.play_quiz() 메서드선택지 개수 변경 (4개 ➔ N개) / 힌트 속성 확장quiz.py의 Quiz 클래스 및 main.py의 add_quiz_flow()입력 유효성 범위 및 예외 처리 정책 변경input_helper.py의 get_valid_int()주요 클래스 및 모듈 명세클래스 / 모듈주요 메서드역할Quizdisplay(idx), is_correct(ans), to_dict(), from_dict()개별 문제 출력, 정답 비교, 직렬화/역직렬화QuizGameload_data(), save_data(), play_quiz(), delete_quiz(idx), show_history()퀴즈 데이터 관리, 파일 입출력, 게임 진행, 최고 점수/기록 관리main.pyprint_menu(), main(), add_quiz_flow(), delete_quiz_flow()CLI 실행 흐름 제어 및 예외 상황 처리input_helper.pyget_valid_int(prompt, min_val, max_val)숫자 입력 검증, 범위 확인, 공백/문자 예외 처리8. 데이터 파일 명세프로그램은 루트 디렉터리의 state.json 파일을 데이터 영속성 저장소로 사용합니다.💡 JSON(JavaScript Object Notation)이란?데이터를 저장하거나 교환할 때 사용하는 텍스트 기반의 경량 데이터 포맷입니다.사람과 컴퓨터 모두 읽고 쓰기 쉬운 { Key : Value } 키-값 쌍 및 배열 구조로 구성됩니다.💡 JSON 포맷을 선택한 이유가독성 & 직관성: 문제, 선택지, 정답이 텍스트 형태로 저장되어 육안으로 데이터를 쉽게 검증하고 편집할 수 있습니다.Python 표준 라이브러리 호환성: 파이썬의 dict 및 list 구조와 1:1로 매핑되어 별도 라이브러리 없이 json 모듈로 직렬화가 가능합니다.경량성 & 무설치 환경: 외부 데이터베이스(DB Server) 없이 단일 파일로 동작하므로 git clone 후 즉시 실행이 가능합니다.state.json 스키마 및 예시JSON{
  "quizzes": [
    {
      "question": "전압, 전류, 저항 사이의 관계를 나타내는 법칙은?",
      "choices": [
        "옴의 법칙",
        "패러데이 법칙",
        "키르히호프 법칙",
        "쿨롱의 법칙"
      ],
      "answer": 1,
      "hint": "기호 V = I * R 로 나타냅니다."
    }
  ],
  "best_score": 100,
  "history": [
    {
      "date": "2026-08-12 17:00:00",
      "total_questions": 5,
      "score": 100
    }
  ]
}
필드명데이터 타입필수 여부설명quizzesArray (Object)필수등록된 퀴즈 객체 목록quizzes[].questionString필수퀴즈 문제 텍스트quizzes[].choicesArray (String)필수4개의 보기 선택지quizzes[].answerInteger필수정답 번호 (1~4)quizzes[].hintString선택힌트 텍스트best_scoreInteger필수역대 최고 점수 기록historyArray (Object)필수최근 게임 플레이 기록 (일시, 문제 수, 점수)9. 파일 저장 정책Atomic Write 적용파일 저장 시 원본 state.json에 직접 덮어쓰지 않고, 임시 파일 state.json.tmp에 먼저 데이터를 기록한 뒤 os.replace()를 호출하여 원자적(Atomic) 교체를 수행합니다.1. state.json.tmp 임시 파일에 새 데이터 기록
2. 저장이 성공적으로 완료되면 os.replace() 실행
3. state.json.tmp ➔ state.json 으로 원자적 파일 교체
이를 통해 프로그램 강제 종료나 정전 등의 상황에서도 기존 데이터 손상을 방지합니다.예외 처리 및 복구 정책상황처리 방식문자열/공백/범위 밖 입력안내 메시지 출력 후 재입력 루프로 안전 복귀Ctrl+C (KeyboardInterrupt)비정상 종료 방지 안내 메시지 출력 후 최신 데이터 저장 및 정상 종료EOFError 발생입력 스트림 종료 감지 후 자동 저장 및 안전 종료state.json 파일 부재최초 실행으로 간주하고 기본 전기 상식 퀴즈 5개 자동 생성state.json 파싱 손상 (JSONDecodeError)기존 손상 파일을 state.json.bak로 백업한 후 기본 데이터로 복구/초기화10. 대량 데이터 확장성 분석현재 단일 JSON 파일을 통째로 읽고 쓰는 방식에서 퀴즈 데이터가 1,000개 이상으로 증가할 경우 다음과 같은 병목이 발생할 수 있습니다.문제점설명I/O 병목퀴즈 1개 추가/삭제 시에도 수천 개의 데이터를 다시 인코딩하여 전체 파일로 덮어써야 함검색 속도 제한특정 퀴즈 검색 시 메모리 내 순차 탐색으로 시간 복잡도 O(N) 소요메모리 오버헤드프로그램 실행 시 모든 퀴즈 데이터를 한 번에 메모리에 적재해야 함개선 방안SQLite DB 전환:관계형 경량 DB로 전환하여 필요한 퀴즈만 쿼리(SELECT)하고, B-Tree 인덱스를 통해 탐색 성능을 O(N)에서 O(log N)으로 최적화합니다.JSON Lines (.jsonl) 포맷 적용:각 퀴즈 객체를 줄바꿈 단위로 관리하여 Append-Only 방식으로 새 문제를 O(1)에 파일 끝에 즉시 추가할 수 있습니다.11. Git 규칙 및 실행 증빙Commit Convention커밋 메시지는 작업 의도를 명확히 파악할 수 있도록 표준 컨벤션을 준수했습니다.타입: 작업 내용 요약
Feat: 새로운 기능 추가 (퀴즈 풀기, 추가, 삭제, 힌트 등)Fix: 버그 및 오류 수정 (모듈 임포트, 인덱스 에러 등)Docs: README.md 문서 및 스크린샷 갱신Refactor: 코드 구조 개선 및 책임 분리Git 브랜치 병합 및 Clone / Pull 실습 증빙1) Git Clone & Pull 실습 터미널 로그# 별도 로컬 환경에서 저장소 복제 실습
$ git clone [https://github.com/juhoo03/python-quiz-game.git](https://github.com/juhoo03/python-quiz-game.git)
Cloning into 'python-quiz-game'...
remote: Enumerating objects: 76, done.
Resolving deltas: 100% (38/38), done.

# 원격 저장소 변경 사항 가져오기 실습
$ git pull origin main
From [https://github.com/juhoo03/python-quiz-game](https://github.com/juhoo03/python-quiz-game)
 * branch            main     -> FETCH_HEAD
Already up to date.
2) Git Commit Log 가지선 그래프 증빙 (10회 이상 커밋 & 병합)12. 새로운 환경에서 설치 및 실행Bash# 1. 저장소 복제
git clone [https://github.com/juhoo03/python-quiz-game.git](https://github.com/juhoo03/python-quiz-game.git)

# 2. 디렉터리 이동
cd python-quiz-game

# 3. 프로그램 실행
python3 main.py