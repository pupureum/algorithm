a, b, c = map(int, input(). split())

if (b >= c):
    n = -1
elif (c - b == 1):
    n = a + 1
else:
    n = a // (c - b) + 1

print (n)