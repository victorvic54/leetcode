class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        queue = matrix[0]
        for i in range(1, len(matrix)):
            tmp_queue = [float('inf')] * len(matrix)
            for j in range(len(queue)):
                if j > 0:
                    tmp_queue[j] = min(tmp_queue[j], queue[j-1] + matrix[i][j])
                if j < len(queue) - 1:
                    tmp_queue[j] = min(tmp_queue[j], queue[j+1] + matrix[i][j])
                
                tmp_queue[j] = min(tmp_queue[j], queue[j] + matrix[i][j])
            queue = tmp_queue

        return min(queue)

