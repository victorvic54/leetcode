class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # kahn algorithm
        adj_list = defaultdict(list)
        indeg = defaultdict(int)
        nodes = set()
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
            nodes.add(u)
            nodes.add(v)
        
        q = deque([])
        for node, degree in indeg.items():
            if degree == 1:
                q.append(node)
        
        while q:
            u = q.popleft()
            nodes.remove(u)
            for v in adj_list[u]:
                indeg[v] -= 1
                if indeg[v] == 1:
                    q.append(v)

        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if u in nodes and v in nodes:
                return [u, v]

        return []

# Time: O(V + E)
# Space: O(V + E)
