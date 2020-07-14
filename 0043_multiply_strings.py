class Solution:
    def getMultiplicationOf(self, num1, digit):
        tmp_result = 0
        
        for i in range(len(num1)):
            tmp_result += int(num1[i]) * digit
            
            if (i == len(num1) - 1):
                return tmp_result
            else:
                tmp_result *= 10
    
    
    def multiply(self, num1: str, num2: str) -> str:
        num1_table = [None] * 11
        num1_table[0] = 0
        
        result = 0
        
        if (len(num1) < len(num2)):
            num2, num1 = num1, num2
        
        for i in range(len(num2)):
            char_num = int(num2[i])
            
            if (not num1_table[char_num]):
                num1_table[char_num] = self.getMultiplicationOf(num1, char_num)
                
            result += num1_table[char_num]
            
            if (i == len(num2) - 1):
                return str(result)
            else:
                result *= 10