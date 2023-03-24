class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connectionMap = defaultdict(list)
        directionMap = defaultdict(list)
        for connection in connections:
            c1, c2 = connection
            connectionMap[c1].append(c2)
            connectionMap[c2].append(c1)
            directionMap[c1].append(c2)
        
        result = 0
        visited_node = set()
        queue = deque([0])
        while queue:
            node = queue.popleft()
            visited_node.add(node)

            for next_node in connectionMap[node]:
                if next_node in visited_node:
                    continue

                if node in directionMap and next_node in directionMap[node]:
                    result += 1

                queue.append(next_node)

        return result

