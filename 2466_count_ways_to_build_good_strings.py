class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high+1):
            if i < zero and i < one:
                continue

            if i >= zero:
                dp[i] += dp[i-zero]
            
            if i >= one:
                dp[i] += dp[i-one]
            
            dp[i] %= MOD

        return sum(dp[low:high+1]) % MOD


    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def backtracking(fulfilled):
            if fulfilled in memo:
                return memo[fulfilled]

            if fulfilled > high:
                return 0

            total_good_str = 0
            if low <= fulfilled <= high:
                total_good_str += 1
            
            total_good_str += backtracking(fulfilled + zero) + backtracking(fulfilled + one)
            total_good_str %= MOD

            memo[fulfilled] = total_good_str
            return total_good_str
        
        return backtracking(0)

