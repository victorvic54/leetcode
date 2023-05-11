class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(0, n1):
            for j in range(0, n2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[n1][n2]


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        self.dp = {}
        return self.backtracking(0, 0)

    def backtracking(self, idx1, idx2):
        if (idx1, idx2) in self.dp:
            return self.dp[(idx1, idx2)]

        if idx1 >= len(self.nums1) or idx2 >= len(self.nums2):
            return 0

        tmp = 0
        if self.nums1[idx1] == self.nums2[idx2]:
            tmp = max(tmp, 1 + self.backtracking(idx1 + 1, idx2 + 1))

        tmp = max(tmp, self.backtracking(idx1 + 1, idx2), self.backtracking(idx1, idx2 + 1))
        self.dp[(idx1, idx2)] = tmp
        return self.dp[(idx1, idx2)]

