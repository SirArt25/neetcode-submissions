class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        info_car = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        for position, speed in info_car:
            time = ((target - position) / speed)
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)