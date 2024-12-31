class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        traveldays = set(days)
        dp = [0] * 366
        for i in range(1, 366):
            if i not in traveldays:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[i-1] + costs[0], 
                    dp[i-7] + costs[1] if i >= 7 else costs[1], 
                    dp[i-30] + costs[2] if i >= 30 else costs[2])
        return dp[-1]


    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def backtracking(idx, covered):
            if idx >= len(days):
                return 0

            if days[idx] <= covered:
                return backtracking(idx + 1, covered)
            
            if (idx, covered) in memo:
                return memo[(idx, covered)]
            
            min_val = float('inf')
            for i in range(len(costs)):
                curr_cost = costs[i] + backtracking(idx + 1, days[idx] + day_cost_len[i] - 1)
                min_val = min(min_val, curr_cost)

            memo[(idx, covered)] = min_val
            return min_val
        return backtracking(0, 0)
