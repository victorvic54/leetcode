class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x:x[0])
        
        min_shot = 0
        prev_range = None
        for i in range(len(sorted_points)):
            if prev_range == None:
                prev_range = sorted_points[i]
                continue
            
            curr_range = sorted_points[i]
            prev_range = [max(prev_range[0], curr_range[0]), min(prev_range[1], curr_range[1])]
            if prev_range[0] > prev_range[1]:
                min_shot += 1
                prev_range = curr_range

        return min_shot + 1
