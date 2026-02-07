class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        b_seen = 0
        for ch in s:
            if ch == 'b':
                b_seen += 1
            else:  # ch == 'a'
                ans = min(ans + 1, b_seen)
        return ans

# Time: O(n)
# Space: O(1)

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = [0] * (n + 1)  # a_count[i] = # of 'a' in s[i:]
        b_count = [0] * (n + 1)  # b_count[i] = # of 'b' in s[i:]

        for i in range(n - 1, -1, -1):
            a_count[i] = a_count[i + 1] + (s[i] == "a")
            b_count[i] = b_count[i + 1] + (s[i] == "b")

        # memo0 for remove_a=False, memo1 for remove_a=True
        memo0 = [-1] * (n + 1)
        memo1 = [-1] * (n + 1)

        def backtracking(idx: int, remove_a: bool) -> int:
            if idx >= n:
                return 0

            if remove_a:
                if memo1[idx] != -1:
                    return memo1[idx]

                if a_count[idx] == 0:
                    memo1[idx] = 0
                else:
                    # delete 'a' if we see it; keep 'b'
                    memo1[idx] = (1 + backtracking(idx + 1, True)) if s[idx] == "a" \
                                 else backtracking(idx + 1, True)
                return memo1[idx]

            else:
                if memo0[idx] != -1:
                    return memo0[idx]

                if a_count[idx] == 0 or b_count[idx] == 0:
                    memo0[idx] = 0
                else:
                    if s[idx] == "b":
                        memo0[idx] = min(
                            backtracking(idx + 1, True),
                            1 + backtracking(idx + 1, False),
                        )
                    else:
                        memo0[idx] = backtracking(idx + 1, False)
                return memo0[idx]

        return backtracking(0, False)

# Time: O(n)
# Space: O(n)
