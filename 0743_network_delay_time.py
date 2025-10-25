class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:    
        # Dijkstra -> cannot be used for negative weights, negative cycles    
        adj_list = defaultdict(list)
        
        for x, y, w in times:
            adj_list[x].append((w, y))
        
        visited = set()
        heap = [(0, k)]
        while heap:
            w1, u = heapq.heappop(heap)
            visited.add(u)
            
            if len(visited) == n:
                return w1
            
            for w2, v in adj_list[u]:
                if v not in visited:
                    heapq.heappush(heap, (w1 + w2, v))
                
        return -1

    # Time: O(V + E Log V)
    # Space: O(V + E)


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Floyd Warshall -> can be used for negative weights, negative cycles
        INF = float('inf')
        dist = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dist[i][i] = 0

        # edges: u -> v with weight w
        for u, v, w in times:
            if w < dist[u][v]:  # in case of multiple edges, keep the smallest
                dist[u][v] = w

        # Floyd–Warshall
        for mid in range(1, n + 1):
            for i in range(1, n + 1):
                if dist[i][mid] == INF:
                    continue
                for j in range(1, n + 1):
                    if dist[mid][j] == INF:
                        continue
                    if dist[i][mid] + dist[mid][j] < dist[i][j]:
                        dist[i][j] = dist[i][mid] + dist[mid][j]

        # Result: longest shortest path from k
        ans = 0
        for i in range(1, n + 1):
            if dist[k][i] == INF:
                return -1
            ans = max(ans, dist[k][i])
        return ans

    # Time: O(V^3)
    # Space: O(V^2)

