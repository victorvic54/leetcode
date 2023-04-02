class Solution:
    def binary_search(self, spell):
        left = 0
        right = len(self.potions)

        while (left < right):
            mid = (left + right) // 2
            if self.potions[mid] * spell < self.success:
                left = mid + 1
            else:
                right = mid
        
        return left

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        self.spells = spells
        self.potions = potions
        self.success = success

        potions.sort()
        right = len(potions)
        result = []

        for spell in spells:
            right = self.binary_search(spell)
            result.append(len(potions) - right)

        return result

