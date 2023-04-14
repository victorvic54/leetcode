class BetterSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        self.memo = {}
        return self.lps(0, len(s) - 1)

    def lps(self, left, right):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left > right:
            return 0
        if left == right:
            return 1

        if self.s[left] == self.s[right]:
            self.memo[(left, right)] = self.lps(left + 1, right - 1) + 2
        else:
            self.memo[(left, right)] = max(self.lps(left, right - 1), self.lps(left + 1, right))
        return self.memo[(left, right)]


class MySolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.string = s
        self.memo = {}

        ans = 0
        for i in range(len(s)):
            ans = max(
                ans,
                self.revolve_around_center(i, i),
                self.revolve_around_center(i, i + 1),
            )
        
        return ans

    def revolve_around_center(self, left, right):
        if left < 0 or len(self.string) <= right:
            return 0

        if left == right:
            return 1 + self.revolve_around_center(left - 1, right + 1)

        if (left, right) in self.memo:
            return self.memo[(left, right)]

        if self.string[left] == self.string[right]:
            self.memo[(left, right)] = 2 + self.revolve_around_center(left - 1, right + 1)
        else:
            self.memo[(left, right)] = max(self.revolve_around_center(left, right + 1), self.revolve_around_center(left - 1, right))
        
        return self.memo[(left, right)]


class BestSolution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

