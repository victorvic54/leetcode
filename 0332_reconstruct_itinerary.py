"""
|  # | Action                              | Heaps after action                     | stack                     | route                          |
| ---- | --------------------------------- | -------------------------------------- | ------------------------- | ------------------------------ |
|  1 | From JFK, pop IFO (smallest) → push | JFK: [VTL], IFO: [VTL], VTL: [IFO,JFK] | [JFK, IFO]                | []                             |
|  2 | From IFO, pop VTL → push            | JFK: [VTL], IFO: [], VTL: [IFO,JFK]    | [JFK, IFO, VTL]           | []                             |
|  3 | From VTL, pop IFO → push            | JFK: [VTL], IFO: [], VTL: [JFK]        | [JFK, IFO, VTL, IFO]      | []                             |
|  4 | IFO has no edges → pop to route     | (unchanged)                            | [JFK, IFO, VTL]           | [IFO]                          |
|  5 | From VTL, pop JFK → push            | JFK: [VTL], IFO: [], VTL: []           | [JFK, IFO, VTL, JFK]      | [IFO]                          |
|  6 | From JFK, pop VTL → push            | JFK: [], IFO: [], VTL: []              | [JFK, IFO, VTL, JFK, VTL] | [IFO]                          |
|  7 | VTL empty → pop to route            | —                                      | [JFK, IFO, VTL, JFK]      | [IFO, VTL]                     |
|  8 | JFK empty → pop to route            | —                                      | [JFK, IFO, VTL]           | [IFO, VTL, JFK]                |
|  9 | VTL empty → pop to route            | —                                      | [JFK, IFO]                | [IFO, VTL, JFK, VTL]           |
| 10 | IFO empty → pop to route            | —                                      | [JFK]                     | [IFO, VTL, JFK, VTL, IFO]      |
| 11 | JFK empty → pop to route            | —                                      | []                        | [IFO, VTL, JFK, VTL, IFO, JFK] |
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer’s and min-heap algorithm
        g = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(g[u], v)        # min-heap → lexicographically smallest first

        route = []                          # will be built in reverse

        def visit(u: str) -> None:
            heap = g[u]
            while heap:
                v = heapq.heappop(heap)     # consume one ticket u->v
                visit(v)

            route.append(u)                 # postorder append

        visit("JFK")
        return route[::-1]

# D = max outdegree of all nodes
# Time: O(E log D)	Each ticket heap-pushed and popped once
# Space: O(E)
