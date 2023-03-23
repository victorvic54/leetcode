class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1

        connection_map = defaultdict(list)
        for connection in connections:
            c1, c2 = connection
            connection_map[c1].append(c2)
            connection_map[c2].append(c1)

        visited_node = set()
        distangled_node = 0
        for i in range(n):
            if i in visited_node:
                continue

            visited_node.add(i)
            distangled_node += 1
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for next_node in connection_map[node]:
                    if next_node in visited_node:
                        continue
                    
                    visited_node.add(next_node)
                    queue.append(next_node)
        
        return distangled_node - 1

