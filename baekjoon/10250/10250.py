for i in range(int(input())):
    H, W, N = map(int, input().split())
    if N % H == 0:
        print(H * 100 + int(N / H))
    else:
        print((N % H) * 100 + int(N / H) + 1)