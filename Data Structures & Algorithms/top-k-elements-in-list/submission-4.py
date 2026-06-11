from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # +1 ensures index = count directly, avoids count-1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):   # skip index 0
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
