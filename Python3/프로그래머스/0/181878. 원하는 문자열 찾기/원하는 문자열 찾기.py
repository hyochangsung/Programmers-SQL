def solution(myString, pat):
    if myString.upper().count(pat.upper()):
        return 1
    else:
        return 0