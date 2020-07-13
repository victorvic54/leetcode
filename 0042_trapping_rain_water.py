'''

Important things to note here is that, your water depends on the max height when moving from left
and max height when moving from right

'''

class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1
        
        maxLeft = 0
        maxRight = 0
        
        result = 0
        
        while (left < right):
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            
            if (maxLeft < maxRight):
                result += maxLeft - height[left]
                left += 1
            else:
                result += maxRight - height[right]
                right -= 1
                
        return result