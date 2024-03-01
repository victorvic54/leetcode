class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = 0
        for char in s:
            if char == "1":
                num_ones += 1
        
        return "1" * (num_ones - 1) + "0" * (len(s) - num_ones) + ("1" if num_ones > 0 else "")
