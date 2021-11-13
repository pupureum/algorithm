iter, max_num = map(int, input().split())
nums = list(map(int, input().split()))
for i in nums:
	if (i< max_num):
		print(i, end=' ')
  
# iter, max = map(int, input().split())
# num = list(map(int, input().split()))
# for i in range(iter):
# 	if num[i] < max:
# 		print(num[i], end=' ')