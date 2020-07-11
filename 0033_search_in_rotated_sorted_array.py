class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        # we want to find the pivot (the smallest number in the array)
        while (lo < hi):
            mid = (lo + hi) // 2
            
            if (nums[mid] > nums[hi]):
                lo = mid + 1
            else:
                hi = mid
        
        # assign as a pivot
        pivot = lo
        
        left = 0
        right = len(nums) - 1
        
        # we want to kind of manipulate the data as if we run binary search in a completely sorted array
        # by changing the number be start at.
        # ex: [5, 6, 7, 8, 1, 3, 4]
        # index 0 is 1, index 1 is 3, index 2 is 4, index 3 is 5;, etc. 
        while (left <= right):
            mid = (left + right) // 2
            real_mid = (mid + pivot) % len(nums)
            
            if (nums[real_mid] == target):
                return real_mid
            else:
                if (nums[real_mid] < target):
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1