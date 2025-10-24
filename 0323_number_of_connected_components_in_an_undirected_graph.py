class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(u):
            visited.add(u)
            for v in adj_list[u]:
                if v not in visited:
                    dfs(v)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components

# Time: O(V + E)
# Space: O(V + E)
#   adj_list (adjacency list)   O(N + E)
#   indeg map   O(N)
#   nodes set   O(N)
#   queue (BFS) O(N)
#   Function call stack (no recursion)  O(1)
