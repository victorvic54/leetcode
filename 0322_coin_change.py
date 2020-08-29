class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([float('inf')] * (amount))
        
        for i in range(1, amount + 1):
            if (i in coins):
                dp[i] = 1
            else:
                for j in range(len(coins)):
                    if (coins[j] > i):
                        continue
                    else:
                        dp[i] = min(dp[i], dp[i-coins[j]] + 1)
                
        if (dp[-1] == float('inf')):
            return -1
        else:
            return dp[-1]