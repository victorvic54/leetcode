class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vertex_colour = [0] * len(graph)
        for i in range(len(graph)):
            if vertex_colour[i] != 0:
                continue
                
            queue = deque([i]) # 1 indicates red, 0 indicates no colour, -1 indicates blue
            vertex_colour[i] = 1

            while queue:
                curr_vertex = queue.popleft()
                for next_vertex in graph[curr_vertex]:
                    if vertex_colour[next_vertex] == 0:
                        vertex_colour[next_vertex] = vertex_colour[curr_vertex] * -1
                        queue.append(next_vertex)
                        continue
                    
                    if vertex_colour[next_vertex] != vertex_colour[curr_vertex] * -1:
                        return False

        return True

