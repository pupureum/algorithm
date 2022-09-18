T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    num = [i for i in range(1, n + 1)]
    
    for x in range(k):
        for j in range(1, n):
            num[j] += num[j - 1]
    print(num[-1])