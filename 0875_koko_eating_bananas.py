class Solution:
    def hours_taken(self, piles, banana_per_hour):
        total_pile = 0
        for pile in piles:
            total_pile += math.ceil(pile / banana_per_hour)
        return total_pile


    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if self.hours_taken(piles, mid) <= H:
                right = mid
            else:
                left = mid + 1
        
        return left

