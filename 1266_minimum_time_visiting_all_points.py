class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0
        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            diagonalTime = min(abs(x2 - x1), abs(y2 - y1))
            straightTime = max(abs(x2 - x1), abs(y2 - y1)) - diagonalTime
            totalTime += diagonalTime + straightTime
        
        return totalTime
