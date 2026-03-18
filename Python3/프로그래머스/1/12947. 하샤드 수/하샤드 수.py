def solution(x):
    num = list(str(x))
    num_sum = 0
    for i in num:
        num_sum += int(i)
    if x % num_sum == 0:
        answer = True
    else:
        answer = False
    return answer