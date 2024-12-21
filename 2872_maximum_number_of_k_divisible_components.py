# Notice that on a node which only have one edge, if it cannot divided by k, it needs to merge with other components
# Time complexity: O(n + m)
#
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        neighbour_nodes = defaultdict(set)
        for x, y in edges:
            neighbour_nodes[x].add(y)
            neighbour_nodes[y].add(x)

        max_components = n
        queue = deque([])
        for node in neighbour_nodes:
            if len(neighbour_nodes[node]) == 1:
                queue.append(node)

        while queue:
            chosen_node = queue.popleft()
            for next_node in neighbour_nodes[chosen_node]:
                if values[chosen_node] % k != 0:
                    values[next_node] += values[chosen_node]
                    max_components -= 1

                neighbour_nodes[next_node].remove(chosen_node)
                if len(neighbour_nodes[next_node]) == 1:
                    queue.append(next_node)
            
            del neighbour_nodes[chosen_node]

        return max_components

