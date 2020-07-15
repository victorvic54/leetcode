'''

This should be the optimal solution for 0051_n_queens problem

'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        col_list = [False] * n
        d_45 = [False] * 2 * n
        d_135 = [False] * 2 * n
        
        def backtracking(row, col_list, d_45, d_135, n, count):
            if (row == n):
                count += 1
            else:
                for col in range(n):
                    # Check the meaning here: https://leetcode.wang/leetCode-52-N-QueensII.html
                    id1 = row + col         # 45 degree
                    id2 = row - col + n     # 135 degree
                    
                    if (col_list[col] or d_45[id1] or d_135[id2]):
                        continue
                        
                    col_list[col] = True
                    d_45[id1] = True
                    d_135[id2] = True
                    
                    count = backtracking(row + 1, col_list, d_45, d_135, n, count);
                    
                    col_list[col] = False
                    d_45[id1] = False
                    d_135[id2] = False
                    
                
            return count
            
        return backtracking(0, col_list, d_45, d_135, n, 0)
