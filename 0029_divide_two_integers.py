class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = dividend / divisor
        
        if (result > 0):
            result = math.floor(result)
        else:
            result = math.ceil(result)
            
        if (result < -1 * 2**31) or (result > 2**31 - 1):
            return 2**31 - 1
        
        return result