words = input().upper()
key = list(set(words))
cnt = []

for i in key:
    cnt.append(words.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
	print(key[cnt.index(max(cnt))])
