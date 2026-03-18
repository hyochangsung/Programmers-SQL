def solution(todo_list, finished):
    answer = []
    for n, i in enumerate(finished):
        if not i:
            answer.append(todo_list[n])
    return answer