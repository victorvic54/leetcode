class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        
        while (left < right):
            distance = right - left
            
            if (height[left] < height[right]):
                result = max(result, distance * height[left])
                left += 1
            else:
                result = max(result, distance * height[right])
                right -= 1
        
        return result