"""
Use these examples for illustration:
Case 1:
[1,1,2,3,3,4,4,5,5]

Case 2:
[1,2,2,3,3,4,4,5,5]

Case 3:
[1,1,2,2,3,3,4,4,5]
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1

        while low < hi:
            mid = (low + hi) // 2
            
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:  # case 1
                return nums[mid]

            if nums[mid-1] == nums[mid]:                               # case 2
                if mid % 2 == 0:
                    hi = mid
                else:
                    low = mid + 1
            else:                                                      # case 3
                if mid % 2 == 0:
                    low = mid + 1
                else:
                    hi = mid

        return nums[low]
