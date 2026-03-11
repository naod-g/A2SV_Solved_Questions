class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                ch = deque()
                digit = deque()
                while stack[-1].isalpha():
                    ch.appendleft(stack.pop())

                stack.pop()
                
                while stack and stack[-1].isdigit():
                    digit.appendleft(stack.pop())
                    
                digit = int("".join(list(digit)))
                ch = "".join(list(ch))

                stack.append(digit * ch)

        return "".join(stack)   