class Quiz:
    def __init__(self, question, choices, answer, hint="힌트가 없습니다."):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def display(self, index):
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data.get("question", ""),
            choices=data.get("choices", []),
            answer=data.get("answer", 1),
            hint=data.get("hint", "힌트가 없습니다.")
        )