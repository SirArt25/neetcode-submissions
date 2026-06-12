class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        suffix = 1
        for i in range(0, len(nums)):
            result[i] = suffix
            suffix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1,  -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        