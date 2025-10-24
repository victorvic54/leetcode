class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        q = deque([])
        for i in range(M):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][N-1] == "O":
                q.append((i, N-1))
        
        for j in range(N):
            if board[0][j] == "O":
                q.append((0, j))
            if board[M-1][j] == "O":
                q.append((M-1, j))
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if board[x][y] != "O":
                    continue
                
                board[x][y] = "E"  # temporary value to save space
                for dx, dy in dirs:
                    if 0 <= x + dx < M and 0 <= y + dy < N and board[x+dx][y+dy] == "O":
                        q.append((x+dx, y+dy))
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == "E":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

# M: rows, N: columns
# Time: O(M x N)
# Space: O(M x N)
