def get_valid_int(prompt, min_val, max_val):
    """지정된 범위 내의 정수를 입력받을 때까지 반복하는 입력 검증 함수"""
    while True:
        try:
            raw_input = input(prompt).strip()
            if not raw_input:
                print("⚠️ 입력값이 없습니다. 다시 입력해주세요.")
                continue
            val = int(raw_input)
            if min_val <= val <= max_val:
                return val
            print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("⚠️ 유효한 숫자를 입력해주세요.")
