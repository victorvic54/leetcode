class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        max_count = 0
        best = 0

        for right, ch in enumerate(s):
            cnt[ch] += 1
            max_count = max(max_count, cnt[ch])

            while (right - left + 1) - max_count > k:
                # max_count will become obsolete and it is fine because
                # unless max_count improve, right - left + 1 will stays the same
                cnt[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best

# Time: O(n)
# Space: O(1)
