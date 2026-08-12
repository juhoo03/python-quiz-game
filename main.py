import sys
from game import QuizGame
from input_helper import get_valid_int

def print_menu():
    print("\n========================================")
    print("      ⚡ 전기 상식 퀴즈 게임 ⚡")
    print("========================================")
    print("1. 퀴즈 풀기 (랜덤 & 힌트)")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록 조회")
    print("4. 최고 점수 & 히스토리 확인")
    print("5. 퀴즈 삭제")
    print("6. 종료")
    print("========================================")

def add_quiz_flow(game):
    print("\n📌 [새로운 퀴즈 추가]")
    question = input("문제를 입력하세요: ").strip()
    while not question:
        print("⚠️ 문제 내용은 비어있을 수 없습니다.")
        question = input("문제를 입력하세요: ").strip()

    choices = []
    for i in range(1, 5):
        choice_text = input(f"선택지 {i}: ").strip()
        while not choice_text:
            print("⚠️ 선택지 내용은 비어있을 수 없습니다.")
            choice_text = input(f"선택지 {i}: ").strip()
        choices.append(choice_text)

    answer = get_valid_int("정답 번호 (1-4): ", 1, 4)
    hint = input("힌트 입력 (없으면 Enter): ").strip()
    if not hint:
        hint = "힌트가 없습니다."

    from quiz import Quiz
    new_quiz = Quiz(question, choices, answer, hint)
    game.quizzes.append(new_quiz)
    game.save_data()
    print("\n✅ 퀴즈가 성공적으로 추가 및 저장되었습니다!")

def show_quizzes_flow(game):
    print("\n📋 [등록된 전체 퀴즈 목록]")
    if not game.quizzes:
        print("현재 등록된 퀴즈가 없습니다.")
        return
    for idx, q in enumerate(game.quizzes, 1):
        print(f"  {idx}. {q.question} (정답: {q.answer}번)")

def delete_quiz_flow(game):
    if not game.quizzes:
        print("\n⚠️ 삭제할 퀴즈가 없습니다.")
        return

    print("\n📋 [삭제할 퀴즈 선택]")
    for idx, quiz in enumerate(game.quizzes, 1):
        print(f"  {idx}. {quiz.question}")

    print("\n삭제할 퀴즈 번호를 입력하세요 (취소: 0)")
    choice = get_valid_int(f"선택 (0~{len(game.quizzes)}): ", 0, len(game.quizzes))

    if choice == 0:
        print("삭제를 취소했습니다.")
        return

    deleted = game.delete_quiz(choice - 1)
    if deleted:
        print(f"\n✅ '{deleted.question}' 문제가 성공적으로 삭제되었습니다!")
    else:
        print("\n⚠️ 삭제 처리에 실패했습니다.")

def main():
    try:
        game = QuizGame()
        while True:
            print_menu()
            choice = get_valid_int("메뉴 선택 (1-6): ", 1, 6)

            if choice == 1:
                game.play_quiz(get_valid_int)
            elif choice == 2:
                add_quiz_flow(game)
            elif choice == 3:
                show_quizzes_flow(game)
            elif choice == 4:
                print(f"\n🏆 역대 최고 점수: {game.best_score}점")
                game.show_history()
            elif choice == 5:
                delete_quiz_flow(game)
            elif choice == 6:
                print("\n👋 프로그램을 안전하게 종료합니다. 이용해 주셔서 감사합니다!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 비정상 입력 감지: 안전하게 데이터 저장 후 종료합니다.")
        game.save_data()
        sys.exit(0)

if __name__ == "__main__":
    main()