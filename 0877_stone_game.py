class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def backtracking(turn, left, right):
            if left == right:
                return 0, piles[left]
            
            if (turn, left, right) in memo:
                return memo[(turn, left, right)]

            if turn == "A":
                alice1, bob1 = backtracking("B", left + 1, right)
                alice2, bob2 = backtracking("B", left, right - 1)

                if alice1 + piles[left] >= alice2 + piles[right]:
                    memo[(turn, left, right)] = alice1 + piles[left], bob1
                else:
                    memo[(turn, left, right)] = alice2 + piles[right], bob2
            else:
                alice1, bob1 = backtracking("A", left + 1, right)
                alice2, bob2 = backtracking("A", left, right - 1)

                if bob1 + piles[left] >= bob2 + piles[right]:
                    memo[(turn, left, right)] = alice1, bob1 + piles[left]
                else:
                    memo[(turn, left, right)] = alice2, bob2 + piles[right]
                
            return memo[(turn, left, right)]


        memo = {}
        alice, bob = backtracking("A", 0, len(piles) - 1)
        return alice > bob

