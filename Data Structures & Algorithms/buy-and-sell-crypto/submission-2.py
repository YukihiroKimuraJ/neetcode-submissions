class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for p in prices:
            lowest = min(lowest, p)
            best = max(best, p - lowest)
        return best
