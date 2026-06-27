import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            operation = operators[token]
            first, second = stack[-2], stack[-1]
            stack.pop()
            stack.pop()
            stack.append(int(operation(first, second)))
        return stack[0]