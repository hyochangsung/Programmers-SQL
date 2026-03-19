def solution(s):
    s = s.lower()
    p_sum = 0
    y_sum = 0
    for i in s:
        if i == 'p':
            p_sum += 1
        elif i == 'y':
            y_sum += 1
    if p_sum != y_sum:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(s)

    return True