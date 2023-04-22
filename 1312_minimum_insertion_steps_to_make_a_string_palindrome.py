class Solution:
    def minInsertions(self, s: str) -> int:
        self.s = s
        self.memo = {}
        self.result = float('inf')
        return self.nextInsertion(0, len(s) - 1)

    def nextInsertion(self, left, right):
        if left >= right:
            return 0
        
        if (left, right) in self.memo:
            return self.memo[(left, right)]

        if self.s[left] == self.s[right]:
            self.memo[(left, right)] = self.nextInsertion(left + 1, right - 1)
        else:
            self.memo[(left, right)] = 1 + min(self.nextInsertion(left + 1, right), self.nextInsertion(left, right - 1))
        
        return self.memo[(left, right)]

        
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            prev = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                prev = temp

        return dp[n-1]
