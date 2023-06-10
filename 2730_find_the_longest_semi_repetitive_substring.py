class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        init = 0
        idx = 1
        result = 0
        prev = None
        while idx < len(s):
            char = s[idx]
            if s[idx-1] == s[idx]:
                if prev == None:
                    prev = idx
                else:
                    result = max(result, idx - init)
                    idx = prev
                    init = prev
                    prev = None
            
            idx += 1

        result = max(result, idx - init)        
        return result
