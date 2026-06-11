from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [[] for _ in range(len(nums))]
        for item, count in counter.items():
            frequency[count-1].append(item)
        topK = []
        for i in range(-1, -len(nums) - 1, -1):
            if len(topK) > k:
                break
            topK.extend(frequency[i])
        return topK[:k]