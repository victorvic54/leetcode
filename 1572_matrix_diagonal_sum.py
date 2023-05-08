class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        max_len = len(mat) - 1
        result = 0
        
        for i in range(len(mat)):
            result += (mat[i][i] + mat[i][max_len-i])
        
        if max_len % 2 == 0:
            result -= mat[i//2][i//2]

        return result
