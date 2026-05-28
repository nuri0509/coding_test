def solution(my_string):
    answer = 0
    
    for element in my_string:
        if element.isdigit():
            answer += int(element)
            
    return answer