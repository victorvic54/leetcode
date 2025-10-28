class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        word_idx = defaultdict(list)
        for i in range(len(s)):
            word_idx[s[i]].append(i)
        
        word_boundaries = []
        for char in word_idx:
            word_boundaries.append((word_idx[char][0], word_idx[char][-1]))
        
        word_boundaries.sort(key=lambda x: x[0])

        #  merge intervals
        merged = []
        curr_start, curr_end = word_boundaries[0]
        for start, end in word_boundaries[1:]:
            if start > curr_end:                 # disjoint: close previous
                merged.append((curr_start, curr_end))
                curr_start, curr_end = start, end
            else:                                # overlap: extend
                curr_end = max(curr_end, end)
        merged.append((curr_start, curr_end))

        return [end - start + 1 for start, end in merged]

"""
Complexity
Building word_idx / boundaries: O(n)
Sorting intervals: O(k log k) where k is the number of unique chars (≤ 26 for lowercase letters)
Merging: O(k)
Time: O(n) time

Space: O(k) space (≈ O(1) for lowercase English)
"""
