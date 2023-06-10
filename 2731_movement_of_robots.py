class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        for i in range(len(nums)):
            if s[i] == "R":
                nums[i] = (nums[i] + d)
            elif s[i] == "L":
                nums[i] = (nums[i] - d)
        
        nums.sort()
        prev = 0
        result = 0
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i-1])
            tmp = (prev + (diff * i)) % MOD
            result = result + tmp
            prev = tmp
        
        return result % MOD

