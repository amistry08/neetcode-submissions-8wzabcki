class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, minPrice = 0, prices[0]
        for i in range(1, len(prices)):
            if (prices[i] > minPrice):
                profit = max(profit, prices[i] - minPrice)
            else:
                minPrice = prices[i]
        return profit