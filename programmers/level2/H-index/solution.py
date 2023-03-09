def solution(citations):
    citationsLen = len(citations)
    citations.sort()
    for i in range(citationsLen):
        if citations[i] >= citationsLen - i: #정렬된 citatopms에서 한칸씩 가다가 그 값이 나머지 길이보다 크거나 같다면
            return citationsLen - i
    return 0

print(solution([3, 0, 6, 1, 5]))