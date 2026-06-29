class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for pos, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temperature:
                pos_x, x = stack.pop()
                result[pos_x] = pos - pos_x
            stack.append((pos, temperature))


        return result