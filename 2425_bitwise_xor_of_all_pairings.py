class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = 0
        if len(nums1) % 2 != 0:
            for num in nums2:
                nums3 ^= num
        
        if len(nums2) % 2 != 0:
            for num in nums1:
                nums3 ^= num
        
        return nums3
