class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtracking(start, target):
            if (start, target) in memo:
                return memo[(start, target)]

            if start == len(nums) and target == 0:
                return 1

            if start >= len(nums):
                return 0
            
            memo[(start, target)] = backtracking(start + 1, target + nums[start]) + \
                                    backtracking(start + 1, target - nums[start])
            return memo[(start, target)]
        return backtracking(0, target)


    # The middle pointer is "total"
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [0] * (2 * total + 1)
        dp[total] = 1
        for i in range(len(nums)):
            next_dp = [0] * (2 * total + 1)
            for tmp_target in range(-total, total + 1):
                if tmp_target + nums[i] + total < 2 * total + 1:
                    next_dp[tmp_target + nums[i] + total] += dp[tmp_target + total]
                
                if tmp_target - nums[i] + total >= 0:
                    next_dp[tmp_target - nums[i] + total] += dp[tmp_target + total]

            dp = next_dp
        return 0 if abs(target) > total else dp[target + total]


    # The middle pointer is "0"
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [0] * (2 * total + 1)
        dp[0] = 1
        for i in range(len(nums)):
            next_dp = [0] * (2 * total + 1)
            for tmp_target in range(-total, total + 1):
                if tmp_target + nums[i] < total + 1:
                    next_dp[tmp_target + nums[i]] += dp[tmp_target]
                
                if tmp_target - nums[i] >= -total:
                    next_dp[tmp_target - nums[i]] += dp[tmp_target]
            dp = next_dp

        return 0 if abs(target) > total else dp[target]


    # The middle pointer is "0"
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = Counter({0: 1})

        for i in range(1, len(nums) + 1):
            tmp_counter = Counter()
            for j in counter:
                tmp_counter[j-nums[i-1]] += counter[j]
                tmp_counter[j+nums[i-1]] += counter[j]
            counter = tmp_counter

        return counter[target]

