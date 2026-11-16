class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands_list = ["+", "-", "*", "/"]
        operands = set(operands_list)
        for token in tokens:
            if token in operands:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]