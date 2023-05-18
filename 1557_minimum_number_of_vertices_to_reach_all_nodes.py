class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        indegree = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1

        ans = []
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)

        return ans


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_list = defaultdict(list)
        for edge in edges:
            edge_list[edge[0]].append(edge[1])

        visited_set = set([i for i in range(n)])
        for i in range(n):
            if i not in visited_set:
                continue

            queue = deque([])
            queue.append(i)
            while queue:
                vertex = queue.popleft()
                for next_vertex in edge_list[vertex]:
                    if next_vertex not in visited_set:
                        continue

                    visited_set.remove(next_vertex)
                    queue.append(next_vertex)
        
        return list(visited_set)

