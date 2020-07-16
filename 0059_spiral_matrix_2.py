'''

Note since the matrix is n * n, we dont need to have a if check when we MoveLeft and MoveUp.
See the difference: 0054_spiral_matrix

'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[-1] * n for _ in range(n)]
        
        max_up = 0
        max_right = n - 1
        max_down = n - 1
        max_left = 0
        
        counter = 1
        max_counter = n * n
        
        while (counter <= max_counter):
            for j in range(max_left, max_right + 1):
                result[max_up][j] = counter
                counter += 1
                
            max_up += 1
            
            for i in range(max_up, max_down + 1):
                result[i][max_right] = counter
                counter += 1
                
            max_right -= 1
            
            for j in range(max_right, max_left - 1, -1):
                result[max_down][j] = counter
                counter += 1
                
            max_down -= 1
            
            for i in range(max_down, max_up - 1, -1):
                result[i][max_left] = counter
                counter += 1
                
            max_left += 1
            
        return result