class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        v = min(nums)
        for x in nums:
            if x % v:
                return 1
        x = nums.count(v)
        return (x + 1) // 2
