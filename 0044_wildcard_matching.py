'''

This is similar problem to 0010_regex_matching

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length_s = len(s) + 1
        length_p = len(p) + 1
        
        dp_arr = [length_p * [False] for i in range(length_s)]
        dp_arr[0][0] = True
        
        for i in range(1, length_p):
            if (p[i-1] != "*"):
                break

            dp_arr[0][i] = True
            
            
        for i in range(1, length_s):
            for j in range(1, length_p):
                if (p[j-1] == s[i-1] or p[j-1] == '?'):
                    dp_arr[i][j] = dp_arr[i-1][j-1]
                elif (p[j-1] == '*'):
                    dp_arr[i][j] = dp_arr[i][j-1] or dp_arr[i-1][j]
                    
        return dp_arr[length_s - 1][length_p - 1]