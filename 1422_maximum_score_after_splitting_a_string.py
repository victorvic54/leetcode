class Solution:
    def maxScore(self, s: str) -> int:
        num_ones = 0
        for char in s:
            if char == "1":
                num_ones += 1
        
        max_val = 0
        num_zeros = 0
        for i in range(len(s) - 1):
            char = s[i]
            if char == "0":
                num_zeros += 1
            else:
                num_ones -= 1
            
            max_val = max(max_val, num_zeros + num_ones)
        
        return max_val
