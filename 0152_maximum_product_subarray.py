from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tmp = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            tmp[i] *= tmp[i - 1] or 1
        
        return max(nums + tmp)