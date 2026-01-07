class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = float('inf')
        num_neg_sign = 0
        total_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    num_neg_sign += 1
                min_val = min(min_val, abs(matrix[i][j]))
                total_sum += abs(matrix[i][j])

        if num_neg_sign % 2 == 0:
            return total_sum

        return total_sum - 2 * min_val

