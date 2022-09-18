input = int(input())

result = input
n = 0
while True:
	result = (result % 10) * 10 + ((result // 10 + result % 10) % 10)
	n += 1
	if (result == input):
		break
print(n)
