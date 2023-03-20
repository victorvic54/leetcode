# My solution here make use of the fact that everytime I see a bed with flower (== 1),
# I will try to count the gap before if and decide how many are there.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [1,0] + flowerbed + [0,1]
        total_flowers = 0
        gap_length = 0
        pos = 0

        while pos < len(flowerbed):
            if flowerbed[pos] == 1:
                total_flowers += max(0, (gap_length - 1) // 2)
                gap_length = 0
                pos += 1
            else:
                while pos < len(flowerbed) and flowerbed[pos] != 1:
                    gap_length += 1
                    pos += 1
            
        return total_flowers >= n

"""
Better solution:
prev | cur
...1 | 0 => can't plant => prev = 0
...0 | 1 => can't plant => prev = 1
...0 | 0 => can plant!! => count++; prev = 1
...1 | 1 => violation!! => count--; prev = 1
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                if prev == 1: # violation!
                    count -= 1
                prev = 1
            else:
                if prev == 1: # can't plant
                    prev = 0 
                else:
                    count += 1
                    prev = 1 # the cur plot gets taken
            
        return count >= n
