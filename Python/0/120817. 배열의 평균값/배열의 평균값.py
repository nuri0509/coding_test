def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
        mean = answer / len(numbers)
    return mean