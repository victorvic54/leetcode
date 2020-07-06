class Solution:
    def intToRoman(self, num: int) -> str:
        key = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        result = ""
        
        for k, v in enumerate(value):
            result += (num // v) * key[k]
            num %= v

        return result