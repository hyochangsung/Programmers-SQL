def solution(numbers):
    sum_num = 0
    for i in range(10):
        if i not in numbers:
            sum_num += i
    return sum_num