'''
Maximum length is len(colors) - 1, so can do check from front and back
'''
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors) - 1
        
        while colors[left] == colors[-1]:
            left += 1
        
        while colors[0] == colors[right]:
            right -= 1
            
        return max(len(colors) - left - 1, right)
