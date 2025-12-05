def solution(s1, s2):
    ans = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] :
                ans += 1
    return ans

