class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def backtracking(next_idx):
            if next_idx in memo:
                return memo[next_idx]

            if next_idx >= len(nums):
                return 0
            
            total = max(nums[next_idx] + backtracking(next_idx + 2), backtracking(next_idx + 1))
            memo[next_idx] = total
            return memo[next_idx]
        
        return backtracking(0)
