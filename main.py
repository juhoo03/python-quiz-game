import sys
from game import QuizGame

def print_menu():
    """메인 메뉴 출력"""
    print("\n===================================")
    print("🎯 나만의 퀴즈 게임 🎯")
    print("===================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 퀴즈 삭제")
    print("6. 종료")
    print("===================================")

def play_quiz(game):
    """1. 퀴즈 풀기 기능 (100점 만점 산출)"""
    if not game.quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다.")
        return

    total_count = len(game.quizzes)
    print(f"\n📝 퀴즈를 시작합니다! (총 {total_count}문제)")
    correct_count = 0

    for i, quiz in enumerate(game.quizzes, 1):
        quiz.display(i)
        
        while True:
            try:
                user_input = input("\n정답 입력: ").strip()
                if not user_input:
                    print("⚠️ 입력이 비어있습니다. 1~4 사이의 숫자를 입력해주세요.")
                    continue
                
                answer_num = int(user_input)
                if not (1 <= answer_num <= 4):
                    print("⚠️ 1~4 사이의 번호만 입력할 수 있습니다.")
                    continue

                if quiz.is_correct(answer_num):
                    print("✅ 정답입니다!")
                    correct_count += 1
                else:
                    print(f"❌ 틀렸습니다! 정답은 {quiz.answer}번입니다.")
                break
            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")

    # 100점 만점 기준 점수 계산
    score = int((correct_count / total_count) * 100)

    print("\n===================================")
    print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")
    if score > game.best_score:
        game.best_score = score
        game.save_data()
        print("🎉 새로운 최고 점수입니다!")
    print("===================================")

def add_quiz(game):
    """2. 퀴즈 추가 기능"""
    print("\n📌 새로운 퀴즈를 추가합니다.")
    question = input("문제를 입력하세요: ").strip()
    while not question:
        print("⚠️ 문제는 빈 값일 수 없습니다.")
        question = input("문제를 입력하세요: ").strip()

    choices = []
    for i in range(1, 5):
        choice = input(f"선택지 {i}: ").strip()
        while not choice:
            print("⚠️ 선택지는 빈 값일 수 없습니다.")
            choice = input(f"선택지 {i}: ").strip()
        choices.append(choice)

    while True:
        try:
            ans_input = input("정답 번호 (1-4): ").strip()
            answer = int(ans_input)
            if 1 <= answer <= 4:
                break
            print("⚠️ 1~4 사이의 숫자만 입력 가능합니다.")
        except ValueError:
            print("⚠️ 숫자만 입력해주세요.")

    from quiz import Quiz
    new_quiz = Quiz(question, choices, answer)
    game.quizzes.append(new_quiz)
    game.save_data()
    print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

def show_quizzes(game):
    """3. 퀴즈 목록 보기"""
    if not game.quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다.")
        return

    print(f"\n📋 등록된 퀴즈 목록 (총 {len(game.quizzes)}개)")
    print("-----------------------------------")
    for i, quiz in enumerate(game.quizzes, 1):
        print(f"[{i}] {quiz.question}")
    print("-----------------------------------")

def show_score(game):
    """4. 최고 점수 확인"""
    print(f"\n🏆 현재 최고 점수: {game.best_score}점")

def delete_quiz(game):
    """5. 퀴즈 삭제 기능"""
    if not game.quizzes:
        print("\n⚠️ 삭제할 퀴즈가 없습니다.")
        return

    show_quizzes(game)
    while True:
        try:
            user_input = input("\n삭제할 퀴즈 번호를 입력하세요 (취소: 0): ").strip()
            if not user_input:
                print("⚠️ 입력이 비어있습니다.")
                continue

            num = int(user_input)
            if num == 0:
                print("취소되었습니다.")
                return

            if 1 <= num <= len(game.quizzes):
                deleted = game.delete_quiz(num - 1)
                print(f"\n✅ [{num}] '{deleted.question}' 퀴즈가 삭제되었습니다!")
                break
            else:
                print(f"⚠️ 1~{len(game.quizzes)} 사이의 번호를 입력해 주세요.")
        except ValueError:
            print("⚠️ 숫자만 입력해주세요.")

def main():
    game = QuizGame()

    while True:
        try:
            print_menu()
            choice = input("선택: ").strip()

            if choice == "1":
                play_quiz(game)
            elif choice == "2":
                add_quiz(game)
            elif choice == "3":
                show_quizzes(game)
            elif choice == "4":
                show_score(game)
            elif choice == "5":
                delete_quiz(game)
            elif choice == "6":
                print("\n게임을 종료합니다. 이용해주셔서 감사합니다! 💕")
                game.save_data()
                break
            else:
                print("\n⚠️ 잘못된 입력입니다. 1~6 사이의 숫자를 입력해주세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 강제 종료 요청이 감지되었습니다. 데이터를 안전하게 저장하고 종료합니다.")
            game.save_data()
            sys.exit(0)

if __name__ == "__main__":
    main()