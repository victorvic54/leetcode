class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        min_val = float('inf')

        for num in nums:
            if num % 2 == 1: # to handle cases where nums only contain odd numbers and make all nums even
                pq.append(-num * 2)
                min_val = min(min_val, num * 2)
            else:
                pq.append(-num)
                min_val = min(min_val, num)

        heapq.heapify(pq)
        min_deviation = float('inf')
        while True:
            max_val = -heapq.heappop(pq)
            min_deviation = min(min_deviation, max_val - min_val)
            if max_val % 2 == 1:
                break

            max_val //= 2
            min_val = min(min_val, max_val)
            heapq.heappush(pq, -max_val)

        return min_deviation
