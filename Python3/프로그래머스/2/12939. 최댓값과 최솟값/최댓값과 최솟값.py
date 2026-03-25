def solution(s):
    s = list(map(int, s.split(" ")))
    max_s = max(s)
    min_s = min(s)
    
    return f"{min_s} {max_s}" 