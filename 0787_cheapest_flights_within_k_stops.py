class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))
        
        queue = deque([(src, 0)])
        visited = [float('inf')] * n
        for _ in range(k+1):
            for _ in range(len(queue)):
                u, w1 = queue.popleft()
                for v, w2 in adj_list[u]:
                    if w1 + w2 < visited[v]:
                        visited[v] = w1 + w2
                        queue.append((v, w1 + w2))
        return visited[dst] if visited[dst] != float('inf') else -1

    """
    E = len(flights) = number of directed edges (flights)
    k = maximum number of stops allowed
    Time: O(E × (k + 1)) = O(kE)
    Space: O(V + E)
    """


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        # (total_cost, node, stops_used)
        pq = [(0, src, 0)]
        # best_stops[u] = fewest stops we've seen so far when reaching u
        best_stops = [float('inf')] * n

        while pq:
            cost, u, stops = heapq.heappop(pq)
            if u == dst:
                return cost
            # stops > best_stops[u]: remember that this is minheap so you get a much smaller cost previously
            if stops > k or stops > best_stops[u]:
                continue
            best_stops[u] = stops
            for v, w in adj_list[u]:
                heapq.heappush(pq, (cost + w, v, stops + 1))

        return -1

    """
    Time: O((E + V) log V) in practice (each push/pop is log V; pruning limits re-expansions)
    Space: O(E + V)
    """
