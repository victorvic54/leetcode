"""
[0] -> 1
[0, 0] -> 3
[0, 0, 0] -> 6
[0, 0, 0, 0] -> 10

Rumus: n * (n + 1) / 2
"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroMaps = defaultdict(int)

        nums = nums + [1] # can put any number except 0 (here I put 1)
        zero_counter = 0

        for num in nums:
            if num != 0:
                if zero_counter != 0:
                    zeroMaps[zero_counter] += 1
                    zero_counter = 0
            else:
                zero_counter += 1

        total = 0
        for counter in zeroMaps:
            total += zeroMaps[counter] * ((counter * (counter + 1)) // 2)
        
        return total

