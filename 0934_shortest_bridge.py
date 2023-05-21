"""
Steps:
1. Get all coordinates of the first island
2. BFS from all of those coordinates
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.grid = grid
        i, j = self.get_first_island_position()

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        first_island = set()
        first_island.add((i, j))

        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for direction in directions:
                x1 = x + direction[0]
                y1 = y + direction[1]
                if not self.validate_new_position(x1, y1):
                    continue

                if self.grid[x1][y1] == 1 and (x1, y1) not in first_island:
                    first_island.add((x1, y1))
                    queue.append((x1, y1))
                    
        visited_set = first_island.copy()
        queue = deque(list(visited_set))
        iteration = 0

        while True:
            tmp_queue = deque([])

            while queue:
                x, y = queue.popleft()
                for direction in directions:
                    x1 = x + direction[0]
                    y1 = y + direction[1]
                    if not self.validate_new_position(x1, y1):
                        continue

                    if (x1, y1) in visited_set:
                        continue
                    
                    if self.grid[x1][y1] == 1:
                        return iteration

                    visited_set.add((x1, y1))
                    tmp_queue.append((x1, y1))

            queue = tmp_queue
            iteration += 1

            if len(queue) == 0:
                break

        return -1


    def validate_new_position(self, x, y):
        if x < 0 or y < 0 or y >= len(self.grid) or x >= len(self.grid[0]):
            return False
        return True


    def get_first_island_position(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    return (i, j)


