class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def backtracking(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(nums):
                return 0
            
            max_money = 0
            max_money = max(max_money, backtracking(idx + 1))
            max_money = max(max_money, nums[idx] + backtracking(idx + 2))
            memo[idx] = max_money
            return max_money
        return backtracking(0)

# Time: O(n)
# Space: O(n)
