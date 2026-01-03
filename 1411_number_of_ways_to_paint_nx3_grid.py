from typing import List, Tuple

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        colors = (0, 1, 2)  # 3 colors, easier than "R/G/B"

        # 1) Generate all valid rows of length 3 (no horizontal adjacency equal)
        valid_rows: List[Tuple[int, int, int]] = []

        def gen_row(pos: int, row: List[int]):
            if pos == 3:
                valid_rows.append(tuple(row))
                return
            for c in colors:
                if pos > 0 and row[pos - 1] == c:
                    continue
                row.append(c)
                gen_row(pos + 1, row)
                row.pop()

        gen_row(0, [])

        # 2) Precompute which rows can follow which (vertical constraints)
        # next_row[j] is allowed after prev_row[i] if all 3 columns differ
        transitions = {r: [] for r in valid_rows}
        for r1 in valid_rows:
            for r2 in valid_rows:
                if r1[0] != r2[0] and r1[1] != r2[1] and r1[2] != r2[2]:
                    transitions[r1].append(r2)

        # 3) Backtracking + memo over row index and previous row
        memo = {}

        def backtrack(row_idx: int, prev_row: Tuple[int, int, int]) -> int:
            if row_idx == n:
                return 1
            key = (row_idx, prev_row)
            if key in memo:
                return memo[key]

            total = 0
            for nxt in transitions[prev_row]:
                total += backtrack(row_idx + 1, nxt)
            total %= MOD
            memo[key] = total
            return total

        # Fake "previous row" that allows any first row:
        # easiest: just sum over starting rows (no vertical constraint for row 0)
        ans = 0
        for start in valid_rows:
            ans += backtrack(1, start)  # we place row 0 as 'start'
        return ans % MOD

# Time: O(n)
# Space: O(n)
