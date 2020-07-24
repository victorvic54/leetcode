class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def DFS(i, j, board, word):
            if len(word) == 0:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False

            tmp = board[i][j]
            board[i][j] = "."
            
            res = DFS(i+1, j, board, word[1:]) or DFS(i-1, j, board, word[1:]) or \
                  DFS(i, j+1, board, word[1:]) or DFS(i, j-1, board, word[1:])
            
            board[i][j] = tmp
            return res
            
        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == word[0]):
                    if (DFS(i, j, board, word)):
                        return True

        return False