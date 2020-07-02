# You will need to draw in the visual way and 
# check how many jumps from the string for each line
# (you will see a jump of multiply 2 from the row and column point of view)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        multiplier = (numRows - 1) * 2
        temp = multiplier
        
        result = ""
        
        if (numRows == 1):
            return s
        
        for i in range(numRows):
            if (i == 0) or (i == numRows - 1):
                result += s[i:len(s):multiplier]
            else:            
                temp -= 2
                
                first = s[i:len(s):multiplier]
                second = s[(i+temp):len(s):multiplier]
                
                temp_ls = [None] * (len(first) + len(second))
                temp_ls[::2] = first
                temp_ls[1::2] = second
                
                result += "".join(temp_ls)
        
        return result
