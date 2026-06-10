class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}

        for i, num in enumerate(nums):
            dict_num[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_num and dict_num[diff] != i:
                return [i, dict_num[diff]]
        return [-1, -1]