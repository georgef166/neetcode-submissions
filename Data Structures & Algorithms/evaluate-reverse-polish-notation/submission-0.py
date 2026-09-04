class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(s2 - s1)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())

            elif c == '/':
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(int(s2 / s1))
            else:
                stack.append(int(c))
        
        return stack[0]
        