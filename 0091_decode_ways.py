class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def backtracking(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(s):
                return 1
            
            total_decodes = 0
            if 1 <= int(s[idx]) <= 9:
                total_decodes += backtracking(idx + 1)
            
            if idx+2 <= len(s) and 10 <= int(s[idx:idx+2]) <= 26:
                total_decodes += backtracking(idx + 2)

            memo[idx] = total_decodes
            return total_decodes
        
        return backtracking(0)

# Time: O(n)
# Space: O(n)


    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1
         
        for i in range(2, len(s) + 1): 
            if (int(s[i - 1]) != 0):   
                dp[i] += dp[i - 1]
                
            if (10 <= int(s[i-2:i]) <= 26): 
                dp[i] += dp[i - 2]

        return dp[-1]
