class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0 , len(heights) - 1
        maxArea = 0

        
        while left < right:
            maxArea = max(maxArea, min(heights[right], heights[left]) * (right - left))
            
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1






        return maxArea