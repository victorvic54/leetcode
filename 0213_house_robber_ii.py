class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def backtracking(idx, first_robbed):
            if (idx, first_robbed) in memo:
                return memo[(idx, first_robbed)]

            if idx >= len(nums):
                return 0

            max_money = 0
            max_money = max(max_money, backtracking(idx + 1, first_robbed))

            if idx != len(nums) - 1 or not first_robbed:
                if idx == 0:
                    max_money = max(max_money, nums[idx] + backtracking(idx + 2, True))
                else:
                    max_money = max(max_money, nums[idx] + backtracking(idx + 2, first_robbed))
            
            memo[(idx, first_robbed)] = max_money
            return max_money
        return backtracking(0, False)

# Time: O(n)
# Space: O(n) -> can be O(1) by return max(backtracking(nums[:-1]), backtracking(nums[1:]))
