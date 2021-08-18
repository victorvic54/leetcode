class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums)):
            result = result ^ i
            result = result ^ nums[i]
            
        return result ^ len(nums)