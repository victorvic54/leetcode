class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        
        if (not nums):
            return result
        
        left = 0
        right = len(nums) - 1
        
        # first binary search to find the left boundary
        while (left < right):
            mid = (left + right) // 2
            
            if (nums[mid] < target):
                left = mid + 1
            else:
                right = mid
        
        # if target can not be found, return [-1, -1]
        if (nums[left] != target):
            return result

        result[0] = left

        # second binary search to find the right boundary
        right = len(nums) - 1
        
        while (left < right):
            # mid is calculated differently
            mid = (left + right + 1) // 2
            
            if (nums[mid] > target):
                right = mid - 1
            else:
                left = mid

        result[1] = left
        
        return result