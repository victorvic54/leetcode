'''

The idea is that for example:
IX -> 1 + 10 - 2 * (1) = 9
XL -> 10 + 50 - 2 * (10) = 40

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        last = None
        
        for roman in s:
            val = roman_to_int_dict[roman]
            result += val
            
            if last and last < val:
                result -= 2 * last
            last = val
        
        return result 