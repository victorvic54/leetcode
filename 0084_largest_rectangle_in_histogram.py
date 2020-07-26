class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_range = [1] * len(heights)
        right_range = [1] * len(heights)
        
        # check for long the bar can be extend to the left from i th position
        for i in range(len(heights)):
            j = i - 1
            
            while (j >= 0):
                if (heights[j] >= heights[i]):
                    left_range[i] += left_range[j]
                    j -= left_range[j]
                else:
                    break
            
        # check for long the bar can be extend to the right from i th position
        for i in range(len(heights) - 1, -1, -1):
            j = i + 1
            
            while (j < len(heights)):
                if (heights[j] >= heights[i]):
                    right_range[i] += right_range[j]
                    j += right_range[j]
                else:
                    break
        
        result = 0
        
        # Example:
        # [2,1,5,6,2,3]
        # 
        # when i = 1, it can be extended to 0 - 5
        # when i = 2, it can be extended to 2 - 3
        for i in range(len(heights)):
            result = max(result, heights[i] * (left_range[i] + right_range[i] - 1))
            
        return result