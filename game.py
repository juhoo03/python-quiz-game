import json
import os
from quiz import Quiz

class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self, filepath="state.json"):
        self.filepath = filepath
        self.quizzes = []
        self.best_score = 0
        self.load_data()  # 게임 생성 시 데이터 불러오기

    def get_default_quizzes(self):
        """기본 전기 관련 퀴즈 데이터 5개 생성"""
        return [
            Quiz("전압, 전류, 저항 사이의 관계를 나타내는 법칙은?", ["옴의 법칙", "패러데이 법칙", "키르히호프 법칙", "쿨롱의 법칙"], 1),
            Quiz("전류의 단위인 암페어의 기본 기호는 무엇일까요?", ["V", "A", "W", "Ω"], 2),
            Quiz("다음 중 전기를 잘 통하게 하는 물질을 무엇이라고 할까요?", ["부도체", "절연체", "도체", "유전체"], 3),
            Quiz("전력(Power)의 단위로 올바른 것은 무엇일까요?", ["볼트(V)", "암페어(A)", "와트(W)", "옴(Ω)"], 3),
            Quiz("건전지처럼 한쪽 방향으로만 흐르는 전류의 종류는?", ["직류(DC)", "교류(AC)", "맥류", "고주파"], 1)
        ]

    def load_data(self):
        """state.json 파일에서 데이터를 불러오거나 초기화하는 메서드"""
        if not os.path.exists(self.filepath):
            # 파일이 없으면 기본 데이터로 초기화
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_data()
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
                
                # 만약 파일에 퀴즈 데이터가 비어있다면 기본 데이터 로드
                if not self.quizzes:
                    self.quizzes = self.get_default_quizzes()
        except Exception:
            # 파일이 손상되었거나 읽을 수 없는 경우 예외 처리
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_data()

    def save_data(self):
        """현재 퀴즈 목록과 최고 점수를 state.json에 저장하는 메서드"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)