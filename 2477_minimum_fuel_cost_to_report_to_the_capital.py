"""
There are two things that you need to keep track.
- One is the fuel (self.ans)
- Another is the number of people you need to carry at a certain point of a node (people)
"""
class Solution:
    def dfs(self, node, prev, people = 1):
        for next_node in self.graph[node]:
            if next_node == prev:
                continue
            people += self.dfs(next_node, node)

        self.ans += (int(ceil(people / self.seats)) if node != 0 else 0)
        return people

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.graph = defaultdict(list)
        for x, y in roads:
            self.graph[x].append(y)
            self.graph[y].append(x)
        
        self.ans = 0
        self.seats = seats
        self.dfs(0, 0)

        return self.ans
