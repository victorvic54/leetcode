class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp.append(questions[-1][0])

        for i in range(len(questions) - 1, -1, -1):
            if (i + questions[i][1] + 1) >= len(questions):
                dp[i] = max(dp[i+1], questions[i][0])
            else:
                dp[i] = max(dp[i+1],  dp[i + questions[i][1] + 1] + questions[i][0])
        
        return dp[0]


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        self.questions = questions
        self.memo = {}
        return self.backtracking(0)

    def backtracking(self, ptr):
        if ptr >= len(self.questions):
            return 0

        if ptr in self.memo:
            return self.memo[ptr]
        
        tmp = max(self.backtracking(ptr + 1), self.questions[ptr][0] + self.backtracking(ptr + self.questions[ptr][1] + 1))
        self.memo[ptr] = tmp
        return tmp

