'''
    Date : 2022년 10월 8일
    Author : 이푸름
    Description: 균형잡힌 세상
'''

while(1):
    data = input()
    stack = []
    result = "yes"
    if data[0] == ".":
        break
    for i in data:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                result = "no"
                break
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                result = "no"
                break
    if len(stack) == 0:
        print(result)
    else:
        print("no")