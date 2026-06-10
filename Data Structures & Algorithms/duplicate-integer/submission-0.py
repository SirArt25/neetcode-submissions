class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        just_set = set()
        for num in nums:
            just_set.add(num)
        return len(just_set) != len(nums)