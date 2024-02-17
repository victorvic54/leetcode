class BestSolution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(len(heights) - 1):
            if heights[i+1] <= heights[i]:
                continue
            
            if len(min_heap) >= ladders and bricks <= 0:
                return i
            
            if len(min_heap) < ladders:
                heapq.heappush(min_heap, heights[i+1] - heights[i])
                continue
            
            if len(min_heap) > 0 and heights[i+1] - heights[i] > min_heap[0]:
                heapq.heappush(min_heap, heights[i+1] - heights[i])
                smallest_height = heapq.heappop(min_heap)
                bricks -= smallest_height
                if bricks < 0:
                    return i
            else:
                bricks -= heights[i+1] - heights[i]
                if bricks < 0:
                    return i

        return len(heights) - 1


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        @lru_cache(None)
        def backtracking(idx, bricks_left, ladders_left):
            if idx == len(heights) - 1:
                return idx

            if heights[idx] >= heights[idx+1]:
                return backtracking(idx + 1, bricks_left, ladders_left)

            ans = idx
            next_step = heights[idx+1] - heights[idx]
            if next_step <= bricks_left:
                ans = max(ans, backtracking(idx + 1, bricks_left - next_step, ladders_left))
            
            if ladders_left > 0:
                ans = max(ans, backtracking(idx + 1, bricks_left, ladders_left - 1))
            
            return ans

        return backtracking(0, bricks, ladders)

