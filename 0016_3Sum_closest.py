class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest_diff = 1e4
        result = 0
        
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                diff = total - target
                
                if (abs(diff) < smallest_diff):
                    smallest_diff = abs(diff)
                    result = total
                    
                if (diff < 0):
                    left += 1
                elif (diff > 0):
                    right -= 1
                else:
                    return result
                    
        return result