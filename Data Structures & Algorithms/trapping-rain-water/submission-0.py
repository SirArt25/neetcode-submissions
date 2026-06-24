class Solution:
    def trap(self, height: List[int]) -> int:
        left_array = [0] * len(height)
        right_array = [0] * len(height)

        max_left = height[0]
        for i in range(len(height)):
            max_left = max(height[i], max_left)
            left_array[i] = max_left

        max_right = height[-1]
        
        for i in range(len(height) - 1, -1 , -1):
            max_right = max(height[i], max_right)
            right_array[i] = max_right

        maxArea = 0

        for i in range(len(height)):
            water = min(right_array[i], left_array[i]) - height[i]
            if water > 0:
                maxArea += water

        return maxArea