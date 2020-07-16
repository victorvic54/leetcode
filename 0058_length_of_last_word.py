class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        result = 0
        
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == ' '):
                return result
            
            result += 1
            
        return result