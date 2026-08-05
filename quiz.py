class Quiz:
    """개별 퀴즈 문제 정보를 관리하는 클래스"""
    
    def __init__(self, question, choices, answer):
        self.question = question    # 문제 (문자열)
        self.choices = choices      # 보기 4개 (리스트)
        self.answer = answer        # 정답 번호 (1~4 정수)

    def display(self, number):
        """퀴즈 문제를 화면에 출력하는 메서드"""
        print(f"\n[문제 {number}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 입력한 답이 정답인지 확인하는 메서드"""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위해 객체를 딕셔너리로 변환하는 메서드"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        """JSON 딕셔너리 데이터를 Quiz 객체로 복원하는 클래스 메서드"""
        return cls(data["question"], data["choices"], data["answer"])