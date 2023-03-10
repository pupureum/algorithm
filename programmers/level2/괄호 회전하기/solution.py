def check(s):
    stack = []
    for i in s:
        if len(stack) == 0: 
            stack.append(i)
        else:
            if i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else: stack.append(i)
    if len(stack) == 0:
        return True
    return False

def solution(s):
    n = len(s)
    answer = 0
    for x in range(n):
        if check(s):
            answer += 1
        s = s[1:] + s[:1]
    return answer

print(solution("[](){}"))