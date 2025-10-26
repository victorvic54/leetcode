class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        memo = {}
        def backtracking(idx, curr_sum):
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]

            if curr_sum == total_sum // 2:
                return True

            if idx >= len(nums) or curr_sum > total_sum // 2:
                return False
            
            can_partition = False
            can_partition = can_partition or backtracking(idx + 1, curr_sum)
            can_partition = can_partition or backtracking(idx + 1, curr_sum + nums[idx])
            memo[(idx, curr_sum)] = can_partition
            return can_partition
        
        return backtracking(0, 0)
            
# Time: O(n × target) — pseudo-polynomial (since target ≤ total_sum/2)
# Space: O(n × target)
