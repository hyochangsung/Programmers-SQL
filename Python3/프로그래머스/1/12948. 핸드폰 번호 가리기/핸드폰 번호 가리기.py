def solution(phone_number):
    fake = (len(phone_number) - 4) * "*"
    real = phone_number[-4:]
    return fake + real