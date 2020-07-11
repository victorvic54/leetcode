'''

Whole picture of this solution is in this image:
https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/next-permutation-algorithm.svg

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        # nums are in descending order
        # ex: 3,2,1  ->  1,2,3
        if i == 0:   
            nums.reverse()
            return 
        
        j = len(nums) - 1
        k = i - 1  # find the last "ascending" position, ex: 1,2,3  -> the number is 2
        
        # we want to find the next number that is bigger than nums[k] in a descending order (check from behind)
        while nums[j] <= nums[k]:
            j -= 1
        
        # swap
        nums[k], nums[j] = nums[j], nums[k]  
        
        # reverse the second part
        l = k+1
        r = len(nums)-1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1