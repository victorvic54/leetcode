# Solution with the help of math

class Solution:
    def reverse(self, x: int) -> int:
        length = len(str(x))
        negative = False
        
        if (str(x)[0] == '-'):
            negative = True
            length -= 1
            x = abs(x)
        
        result = 0
        
        for i in range(length):
            result += (x // (10 ** (length - i - 1))) * (10 ** i)
            x = x % (10 ** (length - i - 1))
        
        
        if (result < -1 * (2**31)) or (result > 2**31 - 1):
            return 0
        else:
            if (negative):
                return result * -1
            else:
                return result
        


# Solution with the help of string

def reverse(self, x: int) -> int:
    new_str = str(x)
    result = None

    if (new_str[0] == '-'):
        temp = new_str[:0:-1]
        result = int('-' + temp)
    else:
        result = int(new_str[::-1])

    if (result < -1 * (2**31)) or (result > 2**31 - 1):
        return 0
    else:
        return result