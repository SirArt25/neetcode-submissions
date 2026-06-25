class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._stack.append((val,val))
            return
        top_a, top_b = self._stack[-1]
        self._stack.append((val,top_b if val > top_b else val))

    def pop(self) -> None:
        if len(self._stack) == 0:
            raise Exception("The stack is empty")
        self._stack.pop()

    def top(self) -> int:
        top_a, top_b = self._stack[-1]
        return top_a

    def getMin(self) -> int:
        top_a, top_b = self._stack[-1]
        return top_b
