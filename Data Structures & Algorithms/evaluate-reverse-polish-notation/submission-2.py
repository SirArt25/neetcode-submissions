import operator 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        for char in tokens:
            if char not in operations:
                stack.append(int(char))
                continue
            operation = operations[char]
            first, second = stack[-2], stack[-1]
            stack.pop()
            stack.pop()
            stack.append(int(operation(first, second)))

        return stack[-1]