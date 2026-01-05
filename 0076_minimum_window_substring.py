from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)         # counts of chars we need
        missing = len(t)          # total chars we still need to match
        left = 0                  # left side of the window
        best_start = 0            # start index of best window
        best_len = float('inf')   # length of best window

        for right, ch in enumerate(s):
            # If we still needed this char, decrement "missing"
            if need[ch] > 0:
                missing -= 1
            # Always decrement need[ch], even if it goes negative
            need[ch] -= 1

            # When we have a valid window (all chars matched)
            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                # Try to shrink from the left
                left_ch = s[left]
                need[left_ch] += 1
                # If we made need[left_ch] positive, we lost a required char
                if need[left_ch] > 0:
                    missing += 1

                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]

# Time: O(|s| + |t|)
# Space: O(|s|)
