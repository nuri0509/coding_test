def solution(my_string, n):
    answer = ""
    for i in range(0,len(my_string)):
        string = my_string[i] * n
        answer += string    
    return answer