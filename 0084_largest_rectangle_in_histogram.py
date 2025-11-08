class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        n = len(heights)
        max_area = 0

        for i in range(n + 1):
            curr_h = heights[i] if i < n else 0

            while s and curr_h < heights[s[-1]]:
                h = heights[s.pop()]
                left_bound = s[-1] if s else -1
                width = i - left_bound - 1
                max_area = max(max_area, width * h)
            
            s.append(i)
        return max_area

"""
Time: O(n)
Space: O(n)

| i | cur_h        | Actions during while-pop                                                           | New stack after step | max_area |
| - | ------------ | ---------------------------------------------------------------------------------- | -------------------- | -------- |
| 0 | 2            | —                                                                                  | `[0]`                | 0        |
| 1 | 1            | pop h=2 → width=1 → area=2 → **max=2**                                             | `[1]`                | 2        |
| 2 | 5            | —                                                                                  | `[1, 2]`             | 2        |
| 3 | 6            | —                                                                                  | `[1, 2, 3]`          | 2        |
| 4 | 2            | pop h=6 → width=1 → area=6 → **max=6**; pop h=5 → width=2 → area=10 → **max=10**   | `[1, 4]`             | 10       |
| 5 | 3            | —                                                                                  | `[1, 4, 5]`          | 10       |
| 6 | 0 (sentinel) | pop h=3 → width=1 → area=3; pop h=2 → width=4 → area=8; pop h=1 → width=6 → area=6 | `[6]`                | 10       |
"""


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
