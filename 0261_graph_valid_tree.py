class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 0:
            return True

        if n != len(edges) + 1:
            return False

        # kahn algorithm
        adj_list = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            if u == v:
                return False

            # edge [a, b] means: to take course a, you must have taken b => [b -> a]
            adj_list[u].append(v)
            adj_list[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        
        q = deque([])
        for i in range(len(indeg)):
            if indeg[i] == 1:
                q.append(i)
        
        visited = 0
        while q:
            u = q.popleft()
            visited += 1
            for v in adj_list[u]:
                indeg[v] -= 1
                if indeg[v] == 1:
                    q.append(v)

        return visited == n

# Time: O(V + E)
# Space: O(V + E)
