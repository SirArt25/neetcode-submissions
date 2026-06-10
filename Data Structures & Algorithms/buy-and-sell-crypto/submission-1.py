class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        l , r = 0, 1
        maxP  = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            r += 1
        return maxP            