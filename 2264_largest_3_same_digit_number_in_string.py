class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        prev = ""

        max_num = ""
        for char in num:
            if char != prev:
                prev = char
                count = 1
                continue
            
            count += 1
            if count == 3:
                max_num = max(max_num, char)
        
        return max_num * 3
