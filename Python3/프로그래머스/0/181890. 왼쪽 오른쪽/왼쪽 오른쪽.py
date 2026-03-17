def solution(str_list):
    for n, i in enumerate(str_list):
        if i == "l":
            print(n, i)
            return str_list[:n]
        elif i == "r":
            return str_list[n+1:]
    return []