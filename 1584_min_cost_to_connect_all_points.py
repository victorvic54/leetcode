class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.sets = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        self.sets -= 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # 1) Build all edges (w, u, v) with Manhattan distance
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                edges.append((w, i, j))

        # 2) Sort edges by weight
        edges.sort(key=lambda e: e[0])

        # 3) Kruskal: greedily take smallest edges that connect new components
        dsu = DSU(n)
        total = 0
        taken = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                total += w
                taken += 1
                if taken == n - 1:  # MST complete
                    break

        return total
    
    """
    Let V be the number of points and E the number of edges.
    Building edges: O(E) (only for the all-pairs version, where E = V²)
    Sorting edges: O(E log E) (for all-pairs, E = V(V−1)/2 ⇒ O(V² log V))
    Union–Find ops: ~O(E · α(n)) ≈ O(E) (α is inverse Ackermann; tiny)

    Total (all-pairs Kruskal) where E = V²:
    Time: O(E log E) 
    Space: O(E) for the edge list
        Edge list	O(V²)
        Union–Find arrays (parent, rank)	O(V)
        Total	O(V²)

    Total (allowed-edges Kruskal):
    Time: O(E log E)
    Space: O(E)

    def kruskal_with_allowed(n: int, allowed_edges: List[tuple[int,int,int]]) -> int:
        # allowed_edges: list of (u, v, w) undirected edges you are allowed to use
        # returns total MST cost; raises ValueError if the graph is disconnected
    
        edges = sorted(allowed_edges, key=lambda e: e[2])  # sort by w
        dsu = DSU(n)
        total, taken = 0, 0
        for u, v, w in edges:
            if dsu.union(u, v):
                total += w
                taken += 1
                if taken == n - 1:
                    return total
        raise ValueError("No MST exists with the allowed edges (graph disconnected).")
    """ 


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm at the very basic case
        n = len(points)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0  # Start from point 0

        total_cost = 0

        for _ in range(n):
            # Choose the unvisited node with smallest connection cost
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            # Add it to the MST
            in_mst[u] = True
            total_cost += min_dist[u]

            # Update distances for the remaining nodes
            for v in range(n):
                if not in_mst[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return total_cost

    # Time: O(V^2)
    # Space: O(V)


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm using min heap easy to understand
        n = len(points)
        min_cost = 0
        visited = set()
        pq = [(0, 0)]  # (cost, vertex)
        cache = {0: 0}

        while pq:
            cost, u = heapq.heappop(pq)
            if u in visited:
                continue

            visited.add(u)
            min_cost += cost

            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < cache.get(v, float('inf')):
                        cache[v] = dist
                        heapq.heappush(pq, (dist, v))

        return min_cost

    # Time: O(V^2 log V)
    # Space: O(V^2) -> you never remove the old (larger) (dist, v) pair from the heap — instead, you just ignore it later when v is visited.

    
