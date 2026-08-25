def solution(angle):
    horizon = 180
    vertical = 90
    
    if angle == horizon :
        answer = 4
    elif angle > vertical : 
        answer = 3  
    elif angle == vertical :
        answer = 2
    else :
        answer = 1
        
    return answer