class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = None
        second = None
        
        left = 0
        
        for i in range(len(nums)):
            num = nums[i]
            
            if (num == first):
                if (num == second):
                    continue
                else:
                    second = num
                    
                    nums[left] = num
                    left += 1
            else:
                first = num
                second = None
                
                nums[left] = num
                left += 1
                
        return left