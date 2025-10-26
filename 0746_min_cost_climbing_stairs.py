class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = {}
        def backtracking(idx):
            if idx in memo:
                return memo[idx]

            if idx <= 1:
                return cost[idx]
            
            min_cost = min(backtracking(idx - 1), backtracking(idx - 2)) + cost[idx]
            memo[idx] = min_cost
            return min_cost

        return backtracking(len(cost) - 1)

# Brute force time: O(2^n)
# Time: O(n)
# Space: O(n)
