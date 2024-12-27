class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left = values[0]  # Best score of values[i] + i seen so far
        max_score = 0         # Global maximum score

        for j in range(1, len(values)):
            max_score = max(max_score, max_left + values[j] - j)
            max_left = max(max_left, values[j] + j)

        return max_score

