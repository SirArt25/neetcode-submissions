class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sets = set()
        for num in nums:
            sets.add(num)
        maxSize = 1
        i = 0
        
        while i < len(nums):
            if nums[i] - 1 not in sets:
                j = nums[i] + 1
                while True:
                    if j not in sets:
                        break
                    j += 1
                maxSize = max(maxSize, j - nums[i])
            i += 1
        return maxSize 