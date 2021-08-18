class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            digit = n & 1
            result = (result + digit) << 1
            n = n >> 1
            
        return result >> 1