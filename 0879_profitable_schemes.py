class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.MOD = 10**9 + 7
        self.dp = {}
        return self.solve(0, 0, 0, n, minProfit, group, profit)

    # k denotes the k-th crime
    # i denotes the i-th group
    # j denotes the j-th profit
    def solve(self, k, i, j, n, minProfit, group, profit):
        if k == len(profit): # it has reached the last crime
            if (j >= minProfit and i <= n): # minimal profit reached and group resources sufficient
                return 1
            return 0

        if (n < i): # resources used more than resource limit
            return 0
        
        if (k, i, j) in self.dp:
            return self.dp[(k, i, j)]
        
        not_include = self.solve(k + 1, i, j, n, minProfit, group, profit)

        # alternative can do this but TLE and since as long as we reach minProfit, we are happy so can optimize
        # include = self.solve(k + 1, i + group[k], j + profit[k], n, minProfit, group, profit)
        include = self.solve(k + 1, i + group[k], min(j + profit[k], minProfit), n, minProfit, group, profit)
        self.dp[(k, i, j)] = (not_include % self.MOD + include % self.MOD) % self.MOD
        return self.dp[(k, i, j)]


"""
Godlike solution

DP:
row -> group
column -> min_profit

  0 1 2 3
0 1 0 0 0
1 0 0 0 0
2 2 2 2 1
3 0 0 0 0
4 1 1 1 1
5 0 0 0 0

Finally sum up all the column of minProfit
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = int(1e9) + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % mod

        return sum(dp[i][minProfit] for i in range(n + 1)) % mod

