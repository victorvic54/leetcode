class Robot:
    def __init__(self, pos):
        self.pos = pos
    
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        directions = [(1, -1), (1, 0), (1, 1)]
        memo = {}

        def dfs(row, robot1, robot2):
            pos1, pos2 = robot1.pos, robot2.pos
            if (row, pos1, pos2) in memo:
                return memo[(row, pos1, pos2)]

            if not (0 <= row < len(grid) and 0 <= pos1 < len(grid[0]) and 0 <= pos2 < len(grid[0])):
                return 0
            
            max_cherries = 0
            for _, dir_y1 in directions:
                for _, dir_y2 in directions:
                    max_cherries = max(
                        max_cherries,
                        dfs(row + 1, Robot(pos1 + dir_y1), Robot(pos2 + dir_y2))
                    )
            
            new_cherries = grid[row][pos1] if pos1 == pos2 else grid[row][pos1] + grid[row][pos2]         
            memo[(row, pos1, pos2)] = new_cherries + max_cherries
            return new_cherries + max_cherries

        return dfs(0, Robot(0), Robot(len(grid[0])-1))

