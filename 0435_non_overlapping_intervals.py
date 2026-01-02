class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end time (earliest finishing first)
        intervals.sort(key=lambda x: x[1])

        removed_count = 0
        last_end_time = -float('inf')

        for start, end in intervals:
            if start >= last_end_time:
                # No overlap — keep this interval
                last_end_time = end
            else:
                # Overlap — remove this one
                removed_count += 1

        return removed_count

# Time: O(n log n)
# Space: O(1)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        memo = {}

        def backtracking(idx, prev_idx):
            if (idx, prev_idx) in memo:
                return memo[(idx, prev_idx)]

            if idx >= len(intervals):
                return 0

            min_removal = float('inf')
            # Option 1: remove current interval
            min_removal = min(min_removal, 1 + backtracking(idx + 1, prev_idx))

            # Option 2: keep current if no overlap
            if prev_idx == -1 or intervals[idx][0] >= intervals[prev_idx][1]:
                min_removal = min(min_removal, backtracking(idx + 1, idx))

            memo[(idx, prev_idx)] = min_removal
            return memo[(idx, prev_idx)]

        return backtracking(0, -1)

# Time: O(n**2)
# Space: O(n**2)
