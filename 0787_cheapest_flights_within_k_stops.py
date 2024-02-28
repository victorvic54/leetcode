# Dijkstra algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        path_map = defaultdict(list)
        for flight in flights:
            from_flight, to_flight, price = flight
            path_map[from_flight].append((to_flight, price))

        queue = deque([(src, 0)]) # (node, price)
        visited = [float('inf')] * n
        visited[src] = 0

        for i in range(k + 1):
            size = len(queue)
            while size > 0:
                source, prev_price = queue.popleft()
                for neighbour, price in path_map[source]:
                    new_price = prev_price + price
                    if new_price < visited[neighbour]:
                        visited[neighbour] = new_price
                        queue.append((neighbour, new_price))
                size -= 1

        return visited[dst] if visited[dst] != float('inf') else -1

