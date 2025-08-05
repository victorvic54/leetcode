class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_count = len(baskets)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    unplaced_count -= 1
                    break

        return unplaced_count

