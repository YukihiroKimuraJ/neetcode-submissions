class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for n in range(len(prices)):
            lowest = min(lowest, prices[n])
            best = max(best, prices[n] - lowest)
        return best