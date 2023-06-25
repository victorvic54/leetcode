class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        prev = None
        diff = []
        
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            if prev != None:
                diff.append(i - prev)

            prev = i
        
        if len(diff) == 0 and prev == None:
            return 0

        result = 1
        for mult in diff:
            result = (result * mult) % MOD
        
        return result
