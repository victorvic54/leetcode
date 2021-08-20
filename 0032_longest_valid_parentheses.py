'''

And the DP idea is :

If s[i] is '(', set dp[i] to 0, because any string end with '(' cannot be a valid one.

Else if s[i] is ')'

     If s[i-1] is '(', dp[i] = dp[i-2] + 2

     Else if s[i-1] is ')' and s[i-dp[i-1]-1] == '(', dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        result = 0
        
        for i in range(1, len(s)):
            if (s[i] == '('):
                dp[i] = 0
            else:
                if (s[i-1] == '('):  # To tackle: ()()  ->  4
                    if (i-2) >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else:  # To tackle: (())  ->  4
                    if (i - dp[i-1] - 1) >= 0 and (s[i - dp[i-1] - 1] == '('):
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                    else:
                        dp[i] = 0

            result = max(result, dp[i])
        
        return result