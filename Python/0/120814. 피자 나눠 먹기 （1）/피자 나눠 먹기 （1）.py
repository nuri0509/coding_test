def solution(n):
    if n < 7 :
        num = 1
    else :
        if n % 7 == 0:
            num = n / 7
        else :
            num = (n // 7) + 1
    return num