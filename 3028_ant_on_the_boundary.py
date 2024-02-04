class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        pos = 0
        for num in nums:
            pos += num
            if pos == 0:
                ans += 1
        return ans

