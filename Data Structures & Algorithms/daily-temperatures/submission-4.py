class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for pos, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                result[stack[-1][0]] = pos - stack[-1][0]
                stack.pop()
            stack.append((pos, temperature))
        return result