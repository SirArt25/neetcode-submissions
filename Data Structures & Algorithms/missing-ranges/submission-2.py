class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        ranges = []
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] > 1:
                ranges.append([nums[i] + 1, nums[i+1] - 1])
        return ranges
        