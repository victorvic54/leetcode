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
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        triplets = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime = [x[0] for x in triplets]
        endTime = [x[1] for x in triplets]
        profit = [x[2] for x in triplets]

        dp = [(0, 0)]
        ans = 0
        for i in range(len(endTime)):
            idx = bisect.bisect_right(dp, startTime[i], key=lambda i: i[0])
            max_profit = max(dp[idx - 1][1] + profit[i], dp[-1][1])
            ans = max(ans, max_profit)
            dp.append((endTime[i], max_profit))
        
        return ans

