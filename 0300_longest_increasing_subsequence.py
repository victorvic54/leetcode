class Solution:
    ####################################
    # (1.0) => O(nlogn) solution, passed
    # Explanation: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn
    ####################################
    def lengthOfLIS(self, nums: List[int]) -> int:
        segment_tree = []
        for i in range(len(nums)):
            if len(segment_tree) == 0 or segment_tree[-1] < nums[i]:
                segment_tree.append(nums[i])
                continue
            
            pos = bisect.bisect_left(segment_tree, nums[i])
            segment_tree[pos] = nums[i]
        
        return len(segment_tree)


    # (1.1) => O(n^2) solution, passed
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
    

    ##################################
    # (1.2) => O(n^2) solution, passed
    ##################################
    def lengthOfLIS(self, nums):
        dp = [None] * len(nums)

        def recurser(prev, start):
            if prev != None and dp[prev] != None:
                return dp[prev]

            if start >= len(nums):
                return 0
        
            ans = 0
            for i in range(start, len(nums)):
                if prev == None or nums[prev] < nums[i]:
                    ans = max(ans, 1 + recurser(i, i + 1))

            if prev != None:
                dp[prev] = ans

            return ans

        return recurser(None, 0) 

    ###################################
    # (1.3) => O(n^2) solution, passed
    ###################################
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def backtracking(prev_idx):
            if prev_idx in memo:
                return memo[prev_idx]

            if prev_idx >= len(nums):
                return 0
            
            max_length = 0
            tmp_nums = nums[prev_idx+1:]
            for i in range(len(tmp_nums)):
                if nums[prev_idx] < tmp_nums[i]:
                    max_length = max(max_length, 1 + backtracking(prev_idx + i + 1))
            memo[prev_idx] = max_length
            return max_length

        max_length = 0        
        for i in range(len(nums)):
            max_length = max(max_length, backtracking(i))
        return 1 + max_length

    #
    #
    #
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

    #################################
    # (6) => This solution is passed
    #################################
    def lengthOfLIS(self, nums):
        dp = [None] * len(nums) # <---- main difference with (5)

        def recurser(prev, start):
            if start >= len(nums):
                return 0
        
            if prev != -1 and dp[prev] != None:
                return dp[prev]

            ans = 0
            if prev == -1 or nums[prev] < nums[start]:
                ans = max(ans, 1 + recurser(start, start + 1))

            ans = max(ans, backtracking(prev, start + 1))
            if prev != -1:
                dp[prev] = ans

            return ans

        return recurser(-1, 0)

