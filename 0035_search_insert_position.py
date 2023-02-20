# O(log n) solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid

        return low


# O(n) solution
class solution:
    def searchinsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if (target <= nums[i]):
                return i
        
        return len(nums)



