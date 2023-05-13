def solution(sizes):
    answer_w = 0
    answer_h = 0

    for i in range(len(sizes)):
        sizes[i].sort()
        answer_w = max(answer_w, sizes[i][0])
        answer_h = max(answer_h, sizes[i][1])
    return answer_h * answer_w

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))