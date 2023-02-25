class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_to_buy = float('inf')
        result = 0

        for price in prices:
            min_to_buy = min(min_to_buy, price)
            result = max(result, price - min_to_buy)

        return result
