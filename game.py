import os
import json
import random
from datetime import datetime
from quiz import Quiz

class QuizGame:
    def __init__(self, filename="state.json"):
        self.filename = filename
        self.quizzes = []
        self.best_score = 0
        self.history = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            self._init_default_data()
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
                self.history = data.get("history", [])
        except (json.JSONDecodeError, KeyError):
            print("⚠️ 데이터 파일이 손상되어 기본 데이터로 초기화합니다.")
            self._init_default_data()

    def save_data(self):
        tmp_filename = f"{self.filename}.tmp"
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": self.history
        }
        try:
            with open(tmp_filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp_filename, self.filename)
        except Exception as e:
            print(f"⚠️ 저장 중 오류 발생: {e}")

    def _init_default_data(self):
        self.quizzes = [
            Quiz("전압, 전류, 저항 사이의 관계를 나타내는 법칙은?", ["옴의 법칙", "패러데이 법칙", "키르히호프 법칙", "쿨롱의 법칙"], 1, "기호 V = I * R 로 나타냅니다."),
            Quiz("전하의 단위는 무엇인가요?", ["볼트(V)", "암페어(A)", "쿨롱(C)", "옴(Ω)"], 3, "기호 C를 사용합니다."),
            Quiz("전류의 단위를 나타내는 기호는?", ["A", "V", "W", "Hz"], 1, "암페어(Ampere)의 약자입니다."),
            Quiz("저항을 직렬 연결하면 전체 저항은 어떻게 되나요?", ["감소한다", "증가한다", "변하지 않는다", "0이 된다"], 2, "R_total = R1 + R2 + ..."),
            Quiz("교류 전원(AC)의 방향은 시간에 따라 어떻게 변하나요?", ["일정하다", "주기적으로 변한다", "랜덤하게 변한다", "0으로 유지된다"], 2, "사인파(Sine wave) 형태로 변화합니다.")
        ]
        self.best_score = 0
        self.history = []
        self.save_data()

    def delete_quiz(self, index):
        """지정한 인덱스의 퀴즈를 삭제하고 파일에 저장합니다."""
        if 0 <= index < len(self.quizzes):
            deleted_quiz = self.quizzes.pop(index)
            self.save_data()
            return deleted_quiz
        return None

    def play_quiz(self, get_valid_input_fn):
        if not self.quizzes:
            print("\n⚠️ 풀 수 있는 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요!")
            return

        total_available = len(self.quizzes)
        print(f"\n📝 전체 {total_available}개 문제 중 몇 문제를 푸시겠습니까?")
        count = get_valid_input_fn(f"문제 수 입력 (1~{total_available}): ", 1, total_available)

        selected_quizzes = random.sample(self.quizzes, count)
        score = 0
        max_possible_score = count * 20

        for idx, quiz in enumerate(selected_quizzes, 1):
            quiz.display(idx)
            print("💡 (힌트를 보려면 'H' 또는 '0'을 입력하세요)")

            while True:
                user_input = input("정답 입력 (1-4, 힌트: H): ").strip().upper()
                if user_input in ['H', '0']:
                    print(f"  👉 [힌트]: {quiz.hint}")
                    continue
                if user_input in ['1', '2', '3', '4']:
                    ans = int(user_input)
                    break
                print("⚠️ 1~4 사이의 숫자 또는 H를 입력해주세요.")

            if quiz.is_correct(ans):
                print("✅ 정답입니다! (+20점)")
                score += 20
            else:
                print(f"❌ 오답입니다! (정답: {quiz.answer}번)")

        print(f"\n========================================")
        print(f"🏆 최종 점수: {score}점 / {max_possible_score}점")

        if score > self.best_score:
            print("🎉 축하합니다! 최고 점수를 갱신하셨습니다!")
            self.best_score = score

        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": count,
            "score": score
        }
        self.history.append(record)
        self.save_data()

    def show_history(self):
        print("\n📜 [최근 게임 플레이 기록 히스토리]")
        if not self.history:
            print("아직 플레이 기록이 없습니다.")
            return

        for idx, h in enumerate(reversed(self.history[-5:]), 1):
            print(f"  [{idx}] {h['date']} | 푼 문제: {h['total_questions']}개 | 점수: {h['score']}점")