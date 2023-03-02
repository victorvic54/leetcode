"""
For n is the number of elements in the nums array:

Analysis for Heap sort solution:
Time complexity: O(n log n)
Space complexity: O(log n)

Analysis for Counting sort solution:
Time complexity: O(n + k) where k is the range of value of its elements (min val to max val)
Space complexity: O(n)

Analysis for Radix sort solution:
We need 10 buckets for each digit (0-9) and we will push array elements in their respective bucket
Time complexity: O(d * (n + b)) where d is the maximum number of digits and b is the size of the bucket used
Space complexity: O(n + b)

Analysis for the below Merge sort solution:
Time complexity: O(n log n)
Space complexity: O(log n + n) = O(n)
"""
class Solution:
    def merge(self, left_nums, right_nums):
        sorted_nums = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left_nums) and right_idx < len(right_nums):
            if left_nums[left_idx] < right_nums[right_idx]:
                sorted_nums.append(left_nums[left_idx])
                left_idx += 1
            else:
                sorted_nums.append(right_nums[right_idx])
                right_idx += 1

        if left_idx < len(left_nums):
            sorted_nums.extend(left_nums[left_idx:])
            return sorted_nums
        
        if right_idx < len(right_nums):
            sorted_nums.extend(right_nums[right_idx:])
            return sorted_nums


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
