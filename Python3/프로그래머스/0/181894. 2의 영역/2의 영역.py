def solution(arr):
    tmp = []
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            tmp.append(i)
    if not tmp:
        return [-1]
    answer = arr[tmp[0]:tmp[-1]+1]  
    return answer