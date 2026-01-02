class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        result = []
        prev_x, prev_y = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > prev_y:
                result.append([prev_x, prev_y])
                prev_x, prev_y = intervals[i]
                continue
            
            prev_x = min(prev_x, intervals[i][0])
            prev_y = max(prev_y, intervals[i][1])
        
        result.append([prev_x, prev_y])
        return result

# Time: O(n log n)
# Space: O(n)
