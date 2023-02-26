'''
There is many solution and explanation out there, but how I come up with the solution
is through drawing the table itself and figure it out.

The dp for word1 = "ros", word2 = "horse":
[[0, 1, 2, 3, 4, 5],
 [1, 1, 2, 2, 3, 4],
 [2, 2, 1, 2, 3, 4],
 [3, 3, 2, 2, 2, 3]]

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word1)
        col = len(word2)
    
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(row + 1):
            dp[i][0] = i
        for j in range(col + 1):
            dp[0][j] = j

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        print(dp)
                    
        return dp[-1][-1]
