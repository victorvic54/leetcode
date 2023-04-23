class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        self.s = s
        self.k = k
        self.dp = {}
        return self.dfs(0)


    def dfs(self, i) -> int:
        if i == len(self.s):
            return 1

        if self.s[i] == '0':
            return 0

        if i in self.dp:
            return self.dp[i]

        ans = 0
        num = 0
        for j in range(i, len(self.s)):
            num = num * 10 + int(self.s[j])
            if num > self.k:
                break
            ans = (ans + self.dfs(j + 1)) % 1000000007

        self.dp[i] = ans
        return ans

