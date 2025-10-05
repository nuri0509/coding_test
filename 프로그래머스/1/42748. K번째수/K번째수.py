def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced = array[i-1:j]       # 1. i~j번째 자르기
        sliced.sort()               # 2. 정렬하기
        answer.append(sliced[k-1])  # 3. k번째 수 추가
    return answer