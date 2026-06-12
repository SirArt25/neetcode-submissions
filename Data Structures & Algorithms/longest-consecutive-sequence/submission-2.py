class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        ans = 1
        if len(nums) == 0:
            return 0
        for x in nums:
            seen.add(x)

        
        for num in seen:
            i = 1
            if num - 1 not in seen:
                while num + i in seen:
                    i+=1
                ans = max(i, ans)

        return ans
