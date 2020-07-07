# Recursive way:

class Solution:
    def pad_string(self, tmp_str: str, result: List[str]):
        new_result = []
       
        for i in range(len(tmp_str)):
            for j in result:
                new_result.append(j + tmp_str[i])
                
        return new_result
            
    
    def letterCombinations(self, digits: str) -> List[str]:
        keypad_dict = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        for i in range(len(digits)):
            tmp_str = keypad_dict[digits[i]]
            
            if (i == 0):
                result = list(tmp_str)
            else:
                result = self.pad_string(tmp_str, result)
            
        return result
    


# Iterative way: (instead of list comprehension, you can make into two for loops)
    
class Solution:    
    def letterCombinations(self, digits):
        keypad_dict = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = [''] if digits else []
        
        for char in digits:
            result = [p + q for p in result for q in keypad_dict[char]]
            
        return result
        