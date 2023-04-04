from collections import Counter

def solution(k, tangerine):
    count = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1])
    answer = 0
    for key, value in count:
        k -= value
        answer += 1
        if k <= 0:
            break
    return answer