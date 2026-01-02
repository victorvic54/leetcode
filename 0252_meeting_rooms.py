"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        prev_end = 0
        for interval in intervals:
            if prev_end > interval.start:
                return False
        
            prev_end = interval.end
        return True

# Time: O(n log n)
# Space: O(1)
