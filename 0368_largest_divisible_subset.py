class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}

        def backtracking(idx, prev_num):
            if (idx, prev_num) in memo:
                return memo[(idx, prev_num)]

            if idx >= len(nums):
                return []

            ans = []
            if prev_num == -1 or nums[idx] % prev_num == 0:
                ans = [nums[idx]] + backtracking(idx + 1, nums[idx])

            tmp_ans = backtracking(idx + 1, prev_num)
            if len(tmp_ans) > len(ans):
                ans = tmp_ans
            
            memo[(idx, prev_num)] = ans
            return ans
        
        return backtracking(0, -1)

