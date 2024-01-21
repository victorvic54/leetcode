class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x -= 1
        y -= 1
        ans = [0] * n
        for i in range(n):
            for j in range(i):
                # x and y as the connector +1
                ans[min(abs(i - j), abs(i - x) + 1 + abs(y - j), abs(i - y) + 1 + abs(x - j)) - 1] += 1
        return [x * 2 for x in ans]


class Solution:
    def bfs(self, path_map, node):
        visited = set()
        visited.add(node)
        
        queue = [node]
        ans = [0] * len(path_map)
        
        counter = 0
        while queue:
            tmp_queue = []
            for node in queue:
                for next_node in path_map[node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        tmp_queue.append(next_node)
                        ans[counter] +=1
            queue = tmp_queue
            counter += 1
        return ans
                
        
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0] * n
        
        path_map = defaultdict(list)
        for i in range(2, n+1):
            path_map[i-1].append(i)
            path_map[i].append(i-1)
        
        if x != y:
            path_map[x].append(y)
            path_map[y].append(x)

        for i in range(1, n+1):
            tmp_ans = self.bfs(path_map, i)
            for j in range(len(ans)):
                ans[j] += tmp_ans[j]
        
        return ans

