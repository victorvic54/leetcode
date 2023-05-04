class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire_lives = 0
        radiant_lives = 0
        for party in senate:
            if party == "D":
                dire_lives += 1
            else:
                radiant_lives += 1

        dire_pass_count = 0
        radiant_pass_count = 0
        queue = deque(senate)
        while queue and dire_lives > 0 and radiant_lives > 0:
            party = queue.popleft()
            if party == "D":
                if dire_pass_count > 0:
                    dire_pass_count -= 1
                    continue

                queue.append("D")
                radiant_pass_count += 1
                radiant_lives -= 1
            else:
                if radiant_pass_count > 0:
                    radiant_pass_count -= 1
                    continue

                queue.append("R")
                dire_pass_count += 1
                dire_lives -= 1

        if dire_lives <= 0:
            return "Radiant"
        else:
            return "Dire"

