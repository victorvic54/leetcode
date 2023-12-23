class Solution:
    def isStrictlyIncreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                return 0
        return 1

    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                result += self.isStrictlyIncreasing(nums[:i] + nums[j:])
        return result

