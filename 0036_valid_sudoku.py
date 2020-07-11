class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row and column check
        for i in range(9):
            tmp_row_set = set()
            tmp_col_set = set()
            
            for j in range(9):
                # row wise
                if (board[i][j] != '.'):
                    if (board[i][j] in tmp_row_set):
                        return False
                
                    tmp_row_set.add(board[i][j])
        
                # column wise
                if (board[j][i] != '.'):
                    if (board[j][i] in tmp_col_set):
                        return False
                    else:
                        tmp_col_set.add(board[j][i])

        # 3x3 grid check
        for col in (0, 3, 6):
            for row in (0, 3, 6):               
                tmp_set = set()
                
                for j in range(3): 
                    tmp_row = row + j

                    for k in range(3):
                        tmp_col = col + k
                        board_val = board[tmp_row][tmp_col]

                        if (board_val != '.'):
                            if (board_val in tmp_set):
                                return False

                            tmp_set.add(board_val)
            
        return True