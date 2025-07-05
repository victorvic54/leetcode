"""
Approach:
(endTime, profit) -> 

[(3, 20)]
[(5, 20)]
[(6, 90)]
[(9, 150)]
[(10, 120)]
"""

class Solution:
    def bisect_left(self, dp, target): # not used, just for learning
        left = 0
        right = len(dp)

        while left < right:
            mid = (left + right) // 2
            if dp[mid][pos] < target:
                left = mid + 1
            else:
                right = mid
        return left


    def bisect_right(self, dp, target, pos):
        left = 0
        right = len(dp)

        while left < right:
            mid = (left + right) // 2
            if dp[mid][pos] <= target:
                left = mid + 1
            else:
                right = mid
        return left


    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        triplets = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime = [x[0] for x in triplets]
        endTime = [x[1] for x in triplets]
        profit = [x[2] for x in triplets]

        dp = [(0, 0)]
        ans = 0
        for i in range(len(endTime)):
            # idx = bisect.bisect_right(dp, startTime[i], key=lambda i: i[0])
            idx = self.bisect_right(dp, startTime[i], 0)
            max_profit = max(dp[idx - 1][1] + profit[i], dp[-1][1])
            ans = max(ans, max_profit)
            dp.append((endTime[i], max_profit))
        
        return ans


    # backtracking no TLE
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_schedules = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        startTime = [x[0] for x in sorted_schedules]
        endTime = [y[1] for y in sorted_schedules]
        profit = [z[2] for z in sorted_schedules]
        
        memo = {}
        def backtracking(start_idx):
            if start_idx >= len(startTime):
                return 0

            if start_idx in memo:
                return memo[start_idx]                
            
            max_profit = 0
            max_profit = max(max_profit, backtracking(start_idx + 1))
            next_start_idx = self.bisectLeft(startTime, endTime[start_idx])
            max_profit = max(max_profit, profit[start_idx] + backtracking(next_start_idx))
            memo[start_idx] = max_profit
            return max_profit
        return backtracking(0)



    # TLE solution backtracking
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def backtracking(next_start_time):
            ans = 0
            for i in range(len(startTime)):
                if startTime[i] < next_start_time:
                    continue

                ans = max(ans, profit[i] + backtracking(endTime[i]))

            return ans
        
        return backtracking(0)

