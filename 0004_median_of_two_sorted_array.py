# Given nums1 and nums2, assign nums1 as a shorter array length
# You want to make a partition based on nums1 and nums2 just need adjust depends on nums1
# Lets say nums1 is divided into left_nums1 and right_nums1, and nums2 is divided into left_nums2 and right_nums2
# We want to make a partition such that (left_nums1 + left_nums2 == right_nums1 + right_nums2) -> for even total array len
# We want to make a partition such that (left_nums1 + left_nums2 + 1 == right_nums1 + right_nums2) -> for odd total array len
# If the above condition is reached
# The result is at line (50 - 53) below

# check youtube video on this or discussion for explanation if you don't get it
# https://youtu.be/LPFhl65R7ww

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_len = len(nums1)
        second_len = len(nums2)
        
        if (second_len < first_len):
            nums1, nums2 = nums2, nums1
            
        low = 0
        high = len(nums1)
        
        while (low <= high):
            partition1 = (low + high) // 2
            partition2 = ((first_len + second_len + 1) // 2) - partition1
            
            if (partition1 == 0):
                min_part1_left = float('-inf')
            else:
                min_part1_left = nums1[partition1 - 1]
            
            if (partition1 == len(nums1)):
                max_part1_right = float('inf')
            else:
                max_part1_right = nums1[partition1]
            
            
            if (partition2 == 0):
                min_part2_left = float('-inf')
            else:
                min_part2_left = nums2[partition2 - 1]
            
            if (partition2 == len(nums2)):
                max_part2_right = float('inf')
            else:
                max_part2_right = nums2[partition2]
            
            
            if (min_part1_left <= max_part2_right) and (min_part2_left <= max_part1_right):
                if (first_len + second_len) % 2 == 0:
                    return (max(min_part1_left, min_part2_left) + min(max_part1_right, max_part2_right)) / 2.0
                else:
                    return max(min_part1_left, min_part2_left)
            elif (min_part2_left > max_part1_right):
                low = partition1 + 1
            else:
                high = partition1 - 1