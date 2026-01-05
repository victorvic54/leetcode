class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = left pointer (candidate buy day)
        # sell = right pointer (current day we consider selling)
        buy = 0
        max_profit = 0

        for sell in range(1, len(prices)):
            # If current price is better (lower) to buy, move the window start
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                # Compute profit with current window [buy .. sell]
                max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit

# Time: O(n)
# Space: O(1)
