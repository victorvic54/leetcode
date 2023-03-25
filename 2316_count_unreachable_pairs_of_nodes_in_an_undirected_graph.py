class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        edge_dict = defaultdict(list)
        for edge in edges:
            e1, e2 = edge
            edge_dict[e1].append(e2)
            edge_dict[e2].append(e1)
        
        visited_set = set()
        connected_components = []
        for i in range(n):
            if i in visited_set:
                continue

            visited_set.add(i)
            connections = [i]
            queue = deque([i])

            while queue:
                node = queue.popleft()
                for next_node in edge_dict[node]:
                    if next_node in visited_set:
                        continue
                    
                    visited_set.add(next_node)
                    queue.append(next_node)
                    connections.append(next_node)

            connected_components.append(connections)
        
        num_missing_links = 0
        for component in connected_components:
            num_missing_links += (n - len(component)) * len(component)
        
        return num_missing_links // 2

