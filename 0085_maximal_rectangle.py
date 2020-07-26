class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if (not matrix):
            return 0

        m = len(matrix)
        n = len(matrix[0])
        
        height_list = [0] * n
        left_list = [0] * n
        right_list = [n] * n
        
        result = 0
        
        for i in range(m):
            curr_left = 0
            curr_right = n
            
            for j in range(n):
                if (matrix[i][j] == '1'):
                    height_list[j] += 1
                else:
                    height_list[j] = 0
                    
            for j in range(n):
                if (matrix[i][j] == '1'):
                    left_list[j] = max(left_list[j], curr_left)
                else:
                    left_list[j] = 0        # we need to add this because the left_list[j] is carried forward to the next row, affecting the max function
                    curr_left = j + 1
                    
            for j in range(n - 1, -1, -1):
                if (matrix[i][j] == '1'):
                    right_list[j] = min(right_list[j], curr_right)
                else:
                    right_list[j] = n       # we need to add this because the right_list[j] is carried forward to the next row, affecting the min function
                    curr_right = j
                    
            for j in range(n):
                result = max(result, (right_list[j] - left_list[j]) * height_list[j])
                
        return result