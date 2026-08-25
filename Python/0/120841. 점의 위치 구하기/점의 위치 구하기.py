def solution(dot):
    x = dot[0]
    y = dot[1]
    quarter = [1, 2, 3, 4] 
    if x > 0 and y > 0 :
        ans = quarter[0]
        
    elif x < 0 and y > 0 :
        ans = quarter[1]
    
    elif x < 0 and y < 0: 
        ans = quarter[2]
            
    else:
        ans = quarter[3]        
    
    return ans
