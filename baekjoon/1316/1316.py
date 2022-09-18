num = int(input())
cnt = 0

for i in range (num):
	word = input()
	if (list(word) == sorted(word, key=word.find)): #알파벳을 찾은 순으로 전부 배열한 리스트와 같아야 그룹단어.
		cnt += 1
print(cnt)