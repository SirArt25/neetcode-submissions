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
            b, a = stack.pop(), stack.pop()   # a is left operand, b is right
            stack.append(int(operation(a, b)))
        return stack[0]