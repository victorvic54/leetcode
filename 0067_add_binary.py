class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_length = len(a) - 1
        b_length = len(b) - 1
    
        carry = 0
        result = ""
        
        while (a_length >= 0 or b_length >= 0 or carry):
            tmp_addition = carry
            
            if (a_length >= 0):
                tmp_addition += int(a[a_length])
            
            if (b_length >= 0):
                tmp_addition += int(b[b_length])

            result = str(tmp_addition % 2) + result
            carry = tmp_addition // 2
            
            a_length -= 1
            b_length -= 1
        
        return result
    
    
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])

