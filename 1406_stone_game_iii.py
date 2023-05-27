# My Solution, all similar structure with stone game 1 and stone game 2
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def backtracking(turn, i):
            if i == n:
                return (0, 0)

            if (turn, i) in memo:
                return memo[(turn, i)]

            alice_score = 0
            bob_score = 0

            score_list = []
            for x in range(1, min(n - i + 1, 4)):
                if turn == "A":
                    alice_score += stoneValue[i + x - 1]
                    alice_tmp_score, bob_tmp_score = backtracking("B", i + x)
                    score_list.append((alice_score + alice_tmp_score, bob_tmp_score))
                else:
                    bob_score += stoneValue[i + x - 1]
                    alice_tmp_score, bob_tmp_score = backtracking("A", i + x)
                    score_list.append((alice_tmp_score, bob_score + bob_tmp_score))

            if turn == "A":
                memo[(turn, i)] = max(score_list, key=lambda x: x[0])
            else:
                memo[(turn, i)] = max(score_list, key=lambda x: x[1])

            return memo[(turn, i)]
        
        alice, bob = backtracking("A", 0)
        if alice == bob:
            return "Tie"
        elif alice > bob:
            return "Alice"
        else:
            return "Bob"


# Cleaner version
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        def f(i):
            if i == n:
                return 0
            result = stoneValue[i] - f(i + 1)
            if i + 2 <= n:
                result = max(result, stoneValue[i] + stoneValue[i + 1] - f(i + 2))
            if i + 3 <= n:
                result = max(result, stoneValue[i] + stoneValue[i + 1]
                            + stoneValue[i + 2] - f(i + 3))
            return result

        dif = f(0)
        if dif > 0:
            return "Alice"
        if dif < 0:
            return "Bob"
        return "Tie"

