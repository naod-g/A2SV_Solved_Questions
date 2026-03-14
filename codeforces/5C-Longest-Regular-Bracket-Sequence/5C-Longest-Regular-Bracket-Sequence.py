s = input()
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])

    elif s[i] == ')':
        x = 0
        while stack and str(stack[-1]).isdigit():
            x += stack.pop()

        if stack and stack[-1] == '(':
            stack.pop()
            while stack and str(stack[-1]).isdigit():
                x += stack.pop()
            stack.append(x + 2)
        else:
            stack.append(x)
            stack.append(s[i])

stack = [s for s in stack if str(s).isdigit()]
mx = 0
for num in stack:
    if num > mx:
        mx = num

if not stack or mx == 0:
    print(0, 1)
else:
    print(mx, stack.count(mx))