def solution(money):
    list = []
    americano = 5500
    cup = money // americano
    extra = money % americano
    list = [cup, extra]
    return list
    