class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -1 * stone)
        
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)

            if first == second:
                continue
            
            heapq.heappush(pq, -1 * abs(first-second))
        
        if len(pq) == 1:
            return abs(heapq.heappop(pq))
        
        return 0

