'''

Tips: Draw the DP table first!

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        tmp_max = nums[0]
        
        for i in range(1, len(nums)):
            tmp_max = max(tmp_max + nums[i], nums[i])
            result = max(result, tmp_max)
            
        return result