class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    curr = 0
                    while stack[-1] != '(':
                        curr = stack.pop() + curr
                    stack.pop()
                    stack.append(2 * curr)

        return sum(stack)
