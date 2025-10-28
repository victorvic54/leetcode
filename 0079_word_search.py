class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def backtracking(pos, idx, visited):
            x, y = pos
            if (x, y) in visited:
                return False

            if board[x][y] != word[idx]:
                return False
            
            if idx + 1 >= len(word):
                return True

            exists = False
            for dx, dy in dirs:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                    # if you do visited | {(x, y)} space complexity becomes O(L^2)
                    visited.add((x, y))
                    exists = exists or backtracking((x+dx, y+dy), idx + 1, visited)
                    visited.remove((x, y))
            return exists
        
        exists = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                exists = exists or backtracking((i, j), 0, set())
        return exists

"""
Let:
m = len(board) (rows)
n = len(board[0]) (columns)
L = len(word)

From each cell, you can move in up to 4 directions (up, down, left, right).
After the first move, you cannot go back to a visited cell, so the branching factor is effectively ≤ 3 per subsequent step.

Thus, in the worst case each start explores roughly:
O(m * n * 3 ^ (L-1))

| Component             | Space    | Explanation                                             |
| --------------------- | -------- | ------------------------------------------------------- |
| Visited set           | O(L)     | Holds up to one entry per character in the current path |
| Recursion stack       | O(L)     | Depth equals the word length                            |
| Total auxiliary space | O(L)     | Visited + recursion                                     |
| Input storage         | O(m·n)   | The board itself (fixed)                                |
Total (including input): O(m·n + L)
"""
