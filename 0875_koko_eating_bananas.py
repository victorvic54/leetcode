class Solution:
    def getHourNeeded(self, piles, k):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / k)
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10**9
        while left < right:
            mid = (left + right) // 2
            if self.getHourNeeded(piles, mid) > h:
                left = mid + 1
            else:
                right = mid
        return left

# Time: O(log (max(piles)) * len(piles)
# Space: O(1)
