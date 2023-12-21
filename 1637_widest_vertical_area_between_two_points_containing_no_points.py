class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = set()
        for x, _ in points:
            x_points.add(x)
        
        x_points = sorted(list(x_points))
        
        max_width = 0
        for i in range(1, len(x_points)):
            max_width = max(max_width, x_points[i] - x_points[i-1])
        
        return max_width
