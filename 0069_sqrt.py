class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while (left <= right):
            mid = (left + right) // 2
            next_mid = mid + 1
            
            if (mid * mid == x) or (mid * mid < x and next_mid * next_mid > x):
                return mid
            elif (mid * mid < x):
                left = mid + 1
            else:
                right = mid - 1