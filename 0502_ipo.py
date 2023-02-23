# Approach:
# Get a map of capital to list of profits, caused constrainted by capital (capital is limited)

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # cannot use defaultdict here otherwise you will get memory limit exceeded (n^2)
        projects = list(zip(capital, profits))
        projects.sort()

        # heapq is a min heap, but we need a max heap, so we will store negated elements
        pq = []
        ptr = 0
        max_ptr = len(profits)

        for i in range(k):
            while ptr < max_ptr and projects[ptr][0] <= w:
                # push a negated element
                heappush(pq, -projects[ptr][1])
                ptr += 1

            if len(pq) == 0:
                break

            # pop a negated element
            w += -heappop(pq)

        return w

