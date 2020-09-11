class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = self.create_dp()
        
    def create_dp(self):
        dp = [[0] * len(self.matrix[0]) for i in range(len(self.matrix))]
        
        for i in range(len(self.matrix)):
            dp[i][0] =  self.matrix[i][0]
        
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                dp[i][j] = dp[i][j-1] + self.matrix[i][j]
        
        if (self.matrix):
            for i in range(1, len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    dp[i][j] += dp[i-1][j]

        return dp


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.dp[row2][col2]
        
        if (row1 - 1 >= 0):
            result -= self.dp[row1-1][col2]
            
        if (col1 - 1 >= 0):
            result -= self.dp[row2][col1-1]
            
        if (col1 - 1 >= 0 and row1 - 1 >= 0):
            result += self.dp[row1-1][col1-1]

        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)