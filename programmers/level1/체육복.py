def solution(n, lost, reserve):
    reserve_uniq = set(reserve) - set(lost)
    lost_uniq = set(lost) - set(reserve)

    for i in reserve_uniq :
        if i-1 in lost_uniq :
            lost_uniq.remove(i-1)
        elif i+1 in lost_uniq :
            lost_uniq.remove(i+1)
        
    return n - len(lost_uniq)

print(solution(4, [1, 2, 3], [2, 3, 4]))