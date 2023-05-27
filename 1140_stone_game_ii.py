"""
- Parameter p determines whose turn it is: if p=0, then Alice moves, otherwise Bob.
- We are only considering the last n-i piles (treat piles[i] as the first pile)
- The current value of the variable M is the number of M piles that you can grab.
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def backtracking(turn, i, m):
            if i == n:
                return 0

            if (turn, i , m) in memo:
                return memo[(turn, i , m)]

            res = 1000000 if turn == "B" else -1
            s = 0

            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if turn == "A":
                    res = max(res, s + backtracking("B", i + x, max(m, x)))
                else:
                    res = min(res, backtracking("A", i + x, max(m, x)))

            memo[(turn, i , m)] = res
            return res
        
        return backtracking("A", 0, 1)

