'''

We view this problem column wise (I fill column-0 first with one queen then column-1, etc.)
This method is not optimal but is easy to understand.
Another method that is optimal is described in 0052_n_queens_2 (scratch idea)

'''

import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        init_board = [['.' for i in range(n)] for j in range(n)]
        
        def is_clashed(x, y, board):
            # We dont need to check for entire column y, since we only fit one queen for each column
            # Check for the entire row x, if there is already a queen
            for j in range(n):
                if (j != y and board[x][j] == 'Q'):
                    return True
            
            
            row_135 = x
            col_135 = y
            
            # check if the 135° diagonal had a queen before.
            while(row_135 >= 0 and col_135 >= 0):
                if (board[row_135][col_135] == 'Q'):
                    return True
                
                row_135 -= 1
                col_135 -= 1
            
            
            row_45 = x
            col_45 = y
            
            # check if the 45° diagonal had a queen before.
            while(row_45 < n and col_45 >= 0):
                if (board[row_45][col_45] == 'Q'):
                    return True
                
                row_45 += 1
                col_45 -= 1
                
                
        def backtracking(j, board):
            if (j == n):  # if reached the last column
                new_board = copy.deepcopy(board)
                modified_board = ["".join(new_board[i]) for i in range(n)]
                
                result.append(modified_board)
            else:
                for i in range(n):
                    if (is_clashed(i, j, board)):
                        continue

                    board[i][j] = 'Q'
                    backtracking(j + 1, board)
                    board[i][j] = '.'
                    
            
        backtracking(0, init_board.copy())
        return result