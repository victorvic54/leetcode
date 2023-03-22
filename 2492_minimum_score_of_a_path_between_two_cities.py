class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited_set = set()

        visited_map = set()
        road_map = defaultdict(list)
        road_cost = defaultdict(int)
        for road in roads:
            start, end, cost = road
            road_map[start].append(end)
            road_map[end].append(start)
            road_cost[(start, end)] = cost
            road_cost[(end, start)] = cost
        
        visited = deque()
        for dest in road_map[1]:
            visited.append((1, dest))

        min_dist = 10000
        while visited:
            start, end = visited.popleft()
            if (start, end) in visited_map:
                continue
            
            visited_map.add((start,end))
            visited_map.add((end,start))
            min_dist = min(min_dist, road_cost[(start, end)])
            for next_node in road_map[end]:
                visited.append((end, next_node))

        return min_dist

