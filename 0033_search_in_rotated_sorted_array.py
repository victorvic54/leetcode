class Solution:
    def binary_search(self, nums, left, right, target):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        if target > nums[-1]:
            target_left = 0
            target_right = left
        else:
            target_left = left
            target_right = len(nums)

        return self.binary_search(nums, target_left, target_right, target)

# Time: O(log n)
# Space: O(1)
