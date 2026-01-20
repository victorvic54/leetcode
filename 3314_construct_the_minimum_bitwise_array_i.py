class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 2:
                continue

            for x in range(nums[i] // 2, nums[i]):
                if x | (x + 1) == nums[i]:
                    ans[i] = x
                    break
        return ans


class BetterSolution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            if not nums[i] % 2:
                continue

            ans[i] = nums[i] - ((nums[i] + 1) & (-nums[i] - 1)) // 2
        
        return ans
