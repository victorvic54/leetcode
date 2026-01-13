class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        left = 0
        right = 10**9

        while abs(left - right) > 10**-5:
            mid = (left + right) / 2

            up_area = 0
            down_area = 0
            for _, y, l in squares:
                if y < mid < y + l:
                    up_area += l * (l - (mid - y))
                    down_area += l * (mid - y)
                elif y >= mid:
                    up_area += l * l
                else:
                    down_area += l * l
            
            if up_area > down_area:
                left = mid
            else:
                right = mid

        return left

# Given n = number of squares
# Time: O(n log (10**9 / 10**-5))
# Space: O(1)
