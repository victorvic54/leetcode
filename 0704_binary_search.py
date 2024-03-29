class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while (left < right):
            center = (left + right) // 2
            
            if (nums[center] == target):
                return center
            elif (nums[center] < target):
                left = center + 1
            else:
                right = center
                    
        return -1
