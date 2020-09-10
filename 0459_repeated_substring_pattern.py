class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
            
        tmp_str = (s + s)[1:-1]
        return tmp_str.find(s) != -1
    
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        for jump in range(1, (len(s) // 2) + 1):
            if (len(s) % jump == 0):
                word_needed = len(s) // jump
                new_text = s[0:jump] * word_needed
                
                if (new_text == s):
                    return True
                
        return False