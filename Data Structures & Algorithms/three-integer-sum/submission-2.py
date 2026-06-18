class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for starting_point, fixed_num in enumerate(nums):
            if fixed_num > 0:
                break
            
            if starting_point > 0 and nums [starting_point] == nums[starting_point-1]:
                continue 
        
            i, j = starting_point + 1, len(nums) - 1
            while i < j:
                target = fixed_num + nums[i] + nums[j]
                if target == 0:
                    results.append((fixed_num, nums[i], nums[j]))
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif target > 0:
                    j -= 1
                else:
                    i += 1
        return results