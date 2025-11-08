class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # potential '3's
        third = float('-inf')  # the best candidate for '2'

        # MAIN IDEA: traverse from right to left
        for num in reversed(nums):
            if num < third:
                return True  # found a valid 1-3-2 pattern
            while stack and num > stack[-1]:
                third = stack.pop()  # update '2' candidate
            stack.append(num)  # push current as potential '3'
        
        return False

# Time: O(n)
# Space: O(n)

"""
[1, 5, 4, 1, -100]
It is better to have [4, 1] than [4, -100]
"""
