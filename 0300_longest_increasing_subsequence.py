class Solution:
    ##################################
    # (1) => O(n^2) solution, passed
    ##################################
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            ans = max(ans, dp[i])
        return ans


    ###########################################
    # (2) => This solution is TLE 22/55 passed
    ############################################
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def backtracking(start, prev):
            if (start, prev) in memo:
                return memo[(start, prev)]

            if start >= len(nums):
                return 0
            
            ans = 0
            if prev == -1 or nums[prev] < nums[start]:
                ans = max(ans, 1 + backtracking(start + 1, start))
            
            ans = max(ans, backtracking(start + 1, prev))
            if prev != -1:
                memo[(start, prev)] = ans
            return memo[(start, prev)]

        return backtracking(0, -1)


    ###########################################
    # (3) => This solution is TLE 53/55 passed
    ###########################################
    def lengthOfLIS(self, nums: List[int]) -> int:
        k = len(nums)
        memo = [[-1] * (k + 1) for _ in range(k + 1)] # <--- using an array instead of using a map

        def backtracking(start, prev):
            if start >= len(nums):
                return 0
            
            if prev != -1 and memo[start][prev] != -1:
                return memo[start][prev]

            ans = 0
            if prev == -1 or nums[prev] < nums[start]:
                ans = max(ans, 1 + backtracking(start + 1, start))
            
            ans = max(ans, backtracking(start + 1, prev))
            if prev != -1:
                memo[start][prev] = ans
            return ans

        return backtracking(0, -1)


    ###############################
    # (4) => This solution passed
    ###############################
    def lengthOfLIS(self, nums: List[int]) -> int:
        k = len(nums)
        memo = [[-1] * (k + 1) for _ in range(k + 1)]

        def backtracking(start, prev):
            if start >= len(nums):
                return 0
            
            if prev != -1 and memo[start][prev] != -1:
                return memo[start][prev]

            ans = 0
            if prev == -1 or nums[prev] < nums[start]:
                ans = 1 + backtracking(start + 1, start) # <--- main difference with (3)
            
            ans = max(ans, backtracking(start + 1, prev))
            if prev != -1:
                memo[start][prev] = ans
            return ans

        return backtracking(0, -1)


    ###########################################
    # (5) => This solution is TLE 22/55 passed
    ###########################################
    def lengthOfLIS(self, nums: List[int]) -> int:
        k = len(nums)
        memo = [[-1] * (k + 1) for _ in range(k + 1)]

        def backtracking(prev, start): # <---- main difference with (4)
            if start >= len(nums):
                return 0
            
            if prev != -1 and memo[prev][start] != -1:
                return memo[prev][start]

            ans = 0
            if prev == -1 or nums[prev] < nums[start]:
                ans = 1 + backtracking(start, start + 1)
            
            ans = max(ans, backtracking(prev, start + 1))
            if prev != -1:
                memo[prev][start] = ans
            return ans

        return backtracking(-1, 0)

