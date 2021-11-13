num = int(input());
for i in range(1, num + 1):
	a, b = map(int, input().split())
	print("Case #", i, ": ", a, " + ", b, " = ", a + b, sep='')
