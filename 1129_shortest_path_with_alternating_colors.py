from collections import deque
class Solution:
    def convert_edge_list_to_map(self, edges):
        result = dict()
        for edge in edges:
            from_node, to_node = edge
            if from_node in result:
                result[from_node].append(to_node)
            else:
                result[from_node] = [to_node]

        return result

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = deque()
        visited_nodes = set([(i, "r") for i in range(1, n)] + [(i, "b") for i in range(1, n)])

        red_edges = self.convert_edge_list_to_map(redEdges)
        blue_edges = self.convert_edge_list_to_map(blueEdges)

        answer = [-1] * n
        answer[0] = 0
        initial_node = 0
        
        if initial_node in red_edges:
            for node in red_edges[initial_node]:
                if node == initial_node:
                    continue

                answer[node] = 1
                q.append((node, 1, "r"))
                visited_nodes.remove((node, "r"))
        
        if initial_node in blue_edges:
            for node in blue_edges[initial_node]:
                if node == initial_node:
                    continue
                answer[node] = 1
                q.append((node, 1, "b"))
                visited_nodes.remove((node, "b"))

        while q:
            prev_node, prev_distance, prev_colour = q.popleft()
            if (prev_colour == "r") and (prev_node in blue_edges) and (blue_edges[prev_node]):
                for node in blue_edges[prev_node]:
                    if (node, "b") not in visited_nodes:
                        continue
                    
                    if answer[node] == -1:
                        answer[node] = prev_distance + 1
                    q.append((node, prev_distance + 1, "b"))
                    visited_nodes.remove((node, "b"))
            
            if (prev_colour == "b") and (prev_node in red_edges) and (red_edges[prev_node]):
                for node in red_edges[prev_node]:
                    if (node, "r") not in visited_nodes:
                        continue
                    
                    if answer[node] == -1:
                        answer[node] = prev_distance + 1
                    q.append((node, prev_distance + 1, "r"))
                    visited_nodes.remove((node, "r"))

        return answer
                

