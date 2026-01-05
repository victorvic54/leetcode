class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def backtracking(idx, can_sell, is_cooldown):
            if (idx, can_sell, is_cooldown) in memo:
                return memo[(idx, can_sell, is_cooldown)]

            if idx >= len(prices):
                return 0
            
            max_profit = 0
            max_profit = max(max_profit, backtracking(idx + 1, can_sell, False))
            if can_sell:
                max_profit = max(max_profit, prices[idx] + backtracking(idx + 1, False, True))
            else:
                if not is_cooldown:
                    max_profit = max(max_profit, -prices[idx] + backtracking(idx + 1, True, False))
            
            memo[(idx, can_sell, is_cooldown)] = max_profit
            return max_profit
        
        return backtracking(0, False, False)

# Time: O(n)
# Space: O(n)

