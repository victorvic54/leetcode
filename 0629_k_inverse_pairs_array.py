class Solution:
    # python memoization (time out)
    # things to know here is that this problem is the same if you reverse the list
    # and check the ascending order pairs
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def backtracking(counter, next_num):
            if counter == k and next_num == n:
                return 1
            
            if counter > k:
                return 0

            if next_num > n:
                return 0
            
            if (counter, next_num) in memo:
                return memo[(counter, next_num)]

            total = 0
            for i in range(next_num + 1):
                total = (total + backtracking(counter + i, next_num + 1)) % MOD
            
            memo[(counter, next_num)] = total
            return total
        
        return backtracking(0, 1)

    # python dp space optimization O(n * k * k), still TLE because I am using python :(
    # n = 1 -> [1]
    # n = 2 -> [1, 1]
    # n = 3 -> [1, 2, 2, 1]
    # n = 4 -> [1, 3, 5, 6, 5, 3, 1] -> capped at k
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k+1)
        dp[0] = 1

        for i in range(0, n):
            tmp_dp = [0] * (k+1)
            for j in range(len(dp)):
                if dp[j] == 0:
                    break
                for x in range(0, i+1):
                    if j+x > k:
                        continue
                    tmp_dp[j+x] = (tmp_dp[j+x] + dp[j]) % MOD
            dp = tmp_dp
        return dp[k]

    # global solution: O(n * k)
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    if j - i < 0:
                        val = dp[i - 1][j]
                    else:
                        val = (dp[i - 1][j] - dp[i - 1][j - i] + MOD) % MOD
                    dp[i][j] = (dp[i][j - 1] + val) % MOD

        
        return (dp[n][k] + MOD - (dp[n][k - 1] if k > 0 else 0)) % MOD

