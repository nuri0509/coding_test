def solution(numbers):
    a = 0
    if a in numbers : 
        numbers.pop(a)
        
    numbers.sort(reverse=True)
    
    first = numbers[0]
    second = numbers[1]
    answer = first * second
    
    return answer