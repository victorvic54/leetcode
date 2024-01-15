class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lose_tracker = defaultdict(int)
        for match in matches:
            winner, loser = match
            players.add(winner)
            players.add(loser)
            lose_tracker[loser] += 1
        
        lose_one = []
        for loser in lose_tracker:
            if lose_tracker[loser] == 1:
                lose_one.append(loser)
            players.remove(loser)
        
        return [sorted(players), sorted(lose_one)]

