class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for sell in range(len(prices)): 
            for buy in range(sell): # buy < sell を保証
                best = max(best, prices[sell] - prices[buy])
        return best