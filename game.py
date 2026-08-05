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
        """기본 퀴즈 데이터 5개 생성"""
        return [
            Quiz("파이썬의 창시자는 누구일까요?", ["Guido", "Linus", "Bjarne", "James"], 1),
            Quiz("파이썬에서 리스트에 요소를 추가할 때 사용하는 메서드는?", ["add()", "append()", "push()", "insert_last()"], 2),
            Quiz("다음 중 파이썬의 변경 불가능한(immutable) 자료형은?", ["list", "dict", "set", "tuple"], 4),
            Quiz("파이썬에서 예외 처리를 위해 사용하는 키워드는?", ["try/except", "do/catch", "try/catch", "error/handle"], 1),
            Quiz("JSON 형식에서 데이터를 저장할 때 사용하는 기본 인코딩 권장 사항은?", ["EUC-KR", "UTF-8", "ASCII", "UTF-16"], 2)
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