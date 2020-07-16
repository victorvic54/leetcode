class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_intervals = sorted(intervals, key=lambda k: k[0])
        
        for interval in sorted_intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result += [interval]

        return result