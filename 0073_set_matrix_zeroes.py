class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        is_first_zero_row = False
        for j in range(col):
            if (matrix[0][j] == 0):
                is_first_zero_row = True
                break
        
        is_first_zero_col = False
        for i in range(row):
            if (matrix[i][0] == 0):
                is_first_zero_col = True
                break
        
        # Label the top row for later decision to zero all the row/col or not
        for i in range(1, row):
            for j in range(1, col):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, row):
            if (matrix[i][0] == 0):
                matrix[i] = [0] * col

        for j in range(1, col):
            if (matrix[0][j] == 0):
                for i in range(row):
                    matrix[i][j] = 0
        
        # Handle whether to zero the entire row or col
        if (is_first_zero_row):
            matrix[0] = [0] * col
            
        if (is_first_zero_col):
            for i in range(row):
                matrix[i][0] = 0