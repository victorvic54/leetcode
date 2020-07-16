class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
            if (interval[0] <= newInterval[1] and interval[1] >= newInterval[0]):
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                result += [interval]

        for i in range(len(result)):
            if (newInterval[0] < result[i][0]):
                result.insert(i, newInterval)
                return result

        result += [newInterval]
        return result