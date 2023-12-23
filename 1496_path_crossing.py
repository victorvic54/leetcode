class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinate = (0, 0)
        path_map = {
            "N": (0,1),
            "S": (0,-1),
            "E": (1,0),
            "W": (-1,0)
        }

        passed = set()
        passed.add(coordinate)
        for wind in path:
            x, y = coordinate
            new_x, new_y = path_map[wind]
            if (x + new_x, y + new_y) in passed:
                return True
            
            coordinate = (x + new_x, y + new_y)
            passed.add(coordinate)
        
        return False
