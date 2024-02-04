class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by ascending x-axis and descending y-axis
        points.sort(key = lambda p: (p[0], -p[1]))
        res = 0
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            m = -inf
            for j in range(i + 1, len(points)):
                xx = points[j][0]
                yy = points[j][1]
                # check for yy > m to avoid prev point m to fall in between yy and y
                # of course yy must be smaller or equal y
                if yy > m and yy <= y:
                    m = yy
                    res += 1
        
        return res
