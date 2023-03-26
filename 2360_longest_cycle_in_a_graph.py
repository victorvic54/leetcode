class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        edge_map = defaultdict(int)
        for i in range(len(edges)):
            next_node = edges[i]
            if next_node == -1:
                continue    
            edge_map[i] = next_node

        max_cycle = -1
        visited_set = set()
        for i in range(len(edges)):
            if i in visited_set:
                continue
            
            counter = 0
            visited_set.add(i)
            cycle_map_index = {i: counter}
            queue = deque([i]) # has at most one node
            while queue:
                node = queue.popleft()
                if node not in edge_map:
                    break
                
                counter += 1
                next_node = edge_map[node]
                
                if next_node in cycle_map_index:
                    max_cycle = max(max_cycle, counter - cycle_map_index[next_node])
                    break

                if next_node in visited_set:
                    break
        
                cycle_map_index[next_node] = counter
                queue.append(next_node)
                visited_set.add(next_node)

        return max_cycle

