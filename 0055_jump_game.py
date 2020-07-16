class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tmp_max = 0
        jump_max = 0
        
        for i in range(len(nums)):
            tmp_max = max(tmp_max, i + nums[i])
            
            if (jump_max >= len(nums) - 1):
                return True
            
            if (i == jump_max):
                jump_max = tmp_max
                
        return False