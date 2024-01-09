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


    # TLE solution backtracking
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def backtracking(next_end_time):
            ans = 0
            for i in range(len(startTime)):
                if startTime[i] < next_end_time:
                    continue

                ans = max(ans, profit[i] + backtracking(endTime[i]))

            return ans
        
        return backtracking(0)

