class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            if not nums[i] % 2:
                continue

            bin_num = bin(nums[i])[2:]
            idx = len(bin_num) - 1
            while idx >= 0:
                if bin_num[idx] == '0':
                    break
                idx -= 1
            ans[i] = int(bin_num[:idx+1] + '0' + bin_num[idx+2:], 2)

        return ans

