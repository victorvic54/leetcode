class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        max_result = -1
        result = 0
        for i in range(len(nums)):
            if i == 0 or i == 1:
                result += nums[i]
                continue

            if nums[i] < result:
                max_result = max(max_result, result + nums[i])

            result += nums[i]

        return max_result

