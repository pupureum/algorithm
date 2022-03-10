X = int(input())

i = 1;
while(X > i):
    X -= i
    i += 1

if (i % 2 == 0):
	a = X
	b = i + 1 - X
else:
    a = i + 1 - X
    b = X

print('{0}/{1}'.format(a, b))