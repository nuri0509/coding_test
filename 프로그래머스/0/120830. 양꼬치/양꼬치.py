def solution(n, k):
    if n < 10 :
        price = 12000 * n + 2000 * k
    
    else :
        free = n // 10
        price = 12000 * n + 2000 * (k - free)     
    
    return price