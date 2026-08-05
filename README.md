# ⚡ 전기 상식 퀴즈 게임 (Python CLI)

> **터미널 환경에서 즐기는 파이썬 기반의 객체지향 전기 상식 퀴즈 게임 프로젝트**  
> *OOP(객체지향), JSON 영속성, 원자적 파일 쓰기(Atomic Write), 입력 검증 예외 처리 완벽 반영*

---

## 1. 프로젝트 개요 및 주제 선정 이유

* **프로젝트 개요**: 객체지향 프로그래밍(OOP) 개념과 JSON 파일 입출력을 활용하여 개발한 콘솔 기반 퀴즈 프로그램입니다.
* **주제 선정 이유**: 일상생활 및 학문적으로 기초가 되는 **'전기 및 회로 기초 지식'**을 재미있게 복습하고 상식을 점검할 수 있도록 전기 상식 퀴즈를 주제로 선정했습니다.

---

## 2. 개발 환경 및 실습 OS 사양

```text
================================================================================
[OS 정보]
$ sw_vers
ProductName:      macOS
ProductVersion:   15.7.4
BuildVersion:     24G517

[쉘 & 터미널]
$ echo $SHELL
/bin/zsh
- mac-os 기본 터미널 (zsh 쉘)

[Docker & 파이썬 개발환경]
$ docker --version
Docker version 28.5.2, build ecc6942 (OrbStack 환경 실행)
Python 버전: Python 3.10 이상 (표준 라이브러리 사용)
================================================================================
3. 주요 기능 및 모듈 호출 흐름📌 주요 기능 목록📝 퀴즈 풀기: 저장된 전기 퀴즈를 풀고 100점 만점 기준 점수 산출📌 퀴즈 추가: 사용자가 문제, 4개 선택지, 정답 번호를 직접 새로 등록 및 저장📋 퀴즈 목록 조회: 현재 저장된 전체 전기 퀴즈 문제 목록 확인🏆 최고 점수 확인: 역대 달성한 최고 점수 기록 유지 및 조회🗑️ 퀴즈 삭제 (보너스 기능): 목록에서 삭제할 퀴즈 번호를 선택하여 삭제 및 실시간 파일 반영💾 데이터 영속성 (state.json): 게임을 종료하거나 재실행해도 state.json에 최신 데이터 자동 저장/복원🛡️ 예외 처리 및 안정성: 잘못된 숫자/문자 입력 방지, Ctrl+C 및 EOFError 강제 종료 시 안전한 자동 저장 처리🔄 모듈 간 호출 흐름 (Sequence / Call Flow)Plaintext┌────────────────────────┐
│   User / CLI Input     │
└───────────┬────────────┘
            │
            ▼
     ┌─────────────┐       (메뉴 선택 및 입력 검증)       ┌───────────────────┐
     │   main.py   │ ─────────────────────────────────► │ input_helper.py   │
     └──────┬──────┘                                    └───────────────────┘
            │
            ├─── 1. play_quiz() ─────► [Quiz.is_correct()] & [score_calculator]
            ├─── 2. add_quiz() ──────► [Quiz] 객체 생성 ──► [QuizGame.quizzes.append()]
            ├─── 3. show_quizzes() ──► [QuizGame.quizzes] 조회
            ├─── 4. show_score() ────► [QuizGame.best_score] 조회
            └─── 5. delete_quiz() ───► [QuizGame.delete_quiz()]
                                                 │
                                                 ▼
                                        ┌───────────────────┐
                                        │ QuizGame.save_data│
                                        └────────┬──────────┘
                                                 │
                                                 ▼ (Atomic Write Process)
                                        ┌───────────────────┐
                                        │  state.json.tmp   │
                                        └────────┬──────────┘
                                                 │ (os.replace)
                                                 ▼
                                        ┌───────────────────┐
                                        │    state.json     │
                                        └───────────────────┘
4. 프로그램 실행 방법Bash# 프로그램 실행
python3 main.py
(별도의 외부 라이브러리 설치 없이 Python 3 기본 표준 라이브러리로 즉시 실행 가능합니다.)5. 클래스 및 구조 설계 근거💡 클래스(OOP) 채택 근거 (VS 절차적 함수 방식)캡슐화 및 상태 관리: Quiz 클래스는 문제, 선택지, 정답 데이터를 단일 객체로 묶어 무분별한 직접 접근을 막고 is_correct() 등의 메서드로 자체 검증을 수행합니다.유지보수성 및 확장성: 단순 Dict/Tuple 기반 관리 시 구조 변경마다 전체 함수를 수정해야 하나, 클래스 도입 시 데이터 구조 변경 시에도 객체 인터페이스만 유지하면 기존 코드의 수정 노력을 최소화할 수 있습니다.🛠️ 주요 클래스 및 모듈 매핑클래스 / 모듈주요 메서드역할 및 책임 예시Quizdisplay(i), is_correct(ans), to_dict()개별 문제 출력, 사용자 정답 비교 및 JSON 저장용 딕셔너리 변환QuizGameload_data(), save_data(), delete_quiz(idx)state.json 읽기/쓰기, 전체 퀴즈 인덱스 관리 및 최고 점수 갱신main.pyprint_menu(), main()CLI 실행 흐름 제어, 사용자 입출력 모듈 호출 및 예외 감지input_helperget_valid_int()사용자 숫자 입력 검증 및 범위 바운드 체크 (재사용성 향상)6. 데이터 파일 명세 (state.json) 및 입출력 정책📋 JSON 파일 명세 (Schema)state.json은 루트 디렉터리에 위치하며 UTF-8 인코딩을 기본으로 지원합니다.JSON{
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
필드명데이터 타입필수 여부설명quizzesArray (Object)필수등록된 퀴즈 객체 목록quizzes[].questionString필수퀴즈 문제 텍스트quizzes[].choicesArray (String)필수4개의 보기 선택지quizzes[].answerInteger (1~4)필수정답 선택지 번호best_scoreInteger필수역대 최고 점수 (백분율)🔍 JSON 포맷 선택 이유가독성 및 경량성: XML 대비 문법 구조가 직관적이어서 사람이 읽고 수정하기 쉬우며, 데이터 구조 크기가 작아 I/O 비용이 적습니다.파이썬 호환성: 파이썬 내장 json 모듈을 통해 Dictionary/List 자료구조와 1:1로 직접 매핑되므로 외부 DB 없이 경량 데이터 관리에 최적입니다.🛡️ 안전한 파일 저장 및 동시성 정책 (Atomic Write)원자적 저장 (Atomic Write): 파일 저장 시 원본 파일에 직접 덮어쓰지 않고 임시 파일(state.json.tmp)에 먼저 기록한 후 os.replace()를 호출해 원본 파일로 교체합니다. 이를 통해 쓰기 작업 도중 프로그램이 종료되더라도 파일 손상을 원천 방지합니다.동시성/충돌 처리: 읽기/쓰기 권한 오류(PermissionError) 시 try/except 블록으로 예외를 안전하게 포착하고 안내 메시지를 출력하여 데이터 손실을 막습니다.🔄 파일 예외 처리 및 자동 백업 / 복구 정책손상 파일 복구: state.json 파싱 실패(JSONDecodeError) 시 기존 파일은 state.json.bak으로 자동 백업한 뒤 기본 퀴즈 5개 데이터로 자동 초기화하여 정상 동작을 보장합니다.기본 데이터 분리: 기본 퀴즈 데이터를 외부 파일(default_quizzes.json)로 분리하여 로드할 수 있도록 예외 옵션을 문서화하였습니다.7. 대량 데이터 확장성 분석 (1,000개 이상 확장 시)현재 구조(단일 state.json 파일 전체 메모리 로딩)에서 문제 수가 1,000개 이상으로 늘어날 경우 다음과 같은 한계와 개선책이 적용될 수 있습니다.성능 및 I/O 병목: 퀴즈 1개 추가/삭제 시 수천 개의 전체 리스트를 직렬화하여 파일 전체를 다시 쓰므로 I/O 병목이 발생합니다.검색 속도 제한: 리스트 순회 기반 조작의 시간 복잡도 $O(N)$ 문제.개선/확장 알고리즘 방안:SQLite DB 전환: RDBMS 전환을 통해 Paging 기법(필요한 개수만큼 로딩) 및 인덱싱($O(\log N)$) 기반 조회 구현.JSON Lines (jsonl) 포맷 적용: 개별 객체를 한 줄 단위로 처리하여 Append-Only 방식으로 파일 전체 재작성 방지.8. Git 규칙 및 실행 증빙 (Log, Clone/Pull)📝 커밋 메시지 작성 규칙 (Commit Convention)컨벤션 구조: 타입: 작업 내용 요약예시:Feat: main.py 입력 검증 헬퍼 함수 분리Fix: game.py delete_quiz 들여쓰기 오류 수정Docs: README.md 실행 증빙 스크린샷 및 명세 보완9. 📸 실행 증빙 스크린샷 (제출 항목)아래 스크린샷은 프로젝트 내 docs/screenshots/ 경로에 수록되어 있습니다.1) 프로그램 실행 증빙 (메뉴 / 퀴즈 풀기 / 추가 / 삭제 / 종료)2) Git Commit Log 증빙 (10회 이상 & 병합 커밋)3) Git Clone / Pull 실습 증빙