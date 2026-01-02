"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap) # Free up rooms that have ended
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

# Time: O(n log n)
# Space: O(n)


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        visited_idx = set()
        result = 0

        while len(visited_idx) != len(intervals):
            last_interval = 0
            for i in range(len(intervals)):
                if i in visited_idx:
                    continue

                interval = intervals[i]
                if last_interval <= interval.start:
                    last_interval = interval.end
                    visited_idx.add(i)
            
            if last_interval != 0:
                result += 1
        
        return result

# Time: O(n**2)
# Space: O(n)
