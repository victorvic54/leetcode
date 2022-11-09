'''
If you keep on calculating the power of n continuously, you will be in a loop
2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True
