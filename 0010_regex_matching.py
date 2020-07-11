'''
Dynamic programming

Side Note: actually we can do this
    for j in range(1, len(s) + 1):
        dp_arr[j][0] = False

but since None or True is always True then, thats okay

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length_s = len(s) + 1
        length_p = len(p) + 1
        
        dp_arr = [length_p * [None] for _ in range(length_s)]
        dp_arr[0][0] = True                                               # empty string is matched with empty string
        
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):
                dp_arr[0][i] = dp_arr[0][i-2]                             # ex: when s = '' and  p = 'z*' 
            else:
                dp_arr[0][i] = False

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if (s[i - 1] == p[j - 1]) or (p[j - 1] == '.'):           # First case: ex: when s = 'aab' and p = 'a..'
                    dp_arr[i][j] = dp_arr[i-1][j-1]
                elif (p[j - 1] == '*'):
                    if (s[i-1] != p[j-2] and p[j-2] != '.'):              # Second case: ex: when s = 'ppi' and p = 'p*.'
                        dp_arr[i][j] = dp_arr[i][j-2]                     #        other ex: when s = 'ab' and p = '.*..'
                    else:                                                 # Third case
                        dp_arr[i][j] = dp_arr[i][j-2] or dp_arr[i-1][j]
                else:
                    dp_arr[i][j] = False
        
        return dp_arr[len(s)][len(p)]
