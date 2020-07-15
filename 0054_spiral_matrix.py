class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if (matrix == []):
            return matrix
        
        max_up = 0
        max_right = len(matrix[0]) - 1
        max_down = len(matrix) - 1
        max_left = 0
        
        result = []
         
        while (max_left <= max_right and max_up <= max_down):
            # Move right
            for j in range(max_left, max_right + 1):
                result.append(matrix[max_up][j])
            
            max_up += 1
            
            # Move down
            for i in range(max_up, max_down + 1):
                result.append(matrix[i][max_right])
            
            max_right -= 1
            
            # If it is in the same row as "Move right", skip
            if (max_up <= max_down):
                # Move left
                for j in range(max_right, max_left - 1, -1):
                    result.append(matrix[max_down][j])

            max_down -= 1
            
            # If it is the same column as "Move down", skip
            if (max_left <= max_right):
                # Move up
                for i in range(max_down, max_up - 1, -1):
                    result.append(matrix[i][max_left])
            
            max_left += 1
            
        return result