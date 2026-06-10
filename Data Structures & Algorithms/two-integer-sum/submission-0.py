class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        
        for i, num in enumerate(nums):
            dict_num[num] = i
        
        for i, num in enumerate(nums):
            te = target - num
            if te in dict_num and dict_num[te] != i:
                return [i, dict_num[te]]  
        
        return [-1, -1]