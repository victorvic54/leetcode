class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        tmp_sum = -float('inf')
        for i in range(len(nums)):
            tmp_sum = max(tmp_sum + nums[i], nums[i])
            max_sum = max(max_sum, tmp_sum)
        return max_sum

# Time: O(n)
# Space: O(1)
