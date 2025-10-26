class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        max_word_len = 20

        memo = {}
        def backtracking(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(s):
                return True
            
            can_word_break = False
            for i in range(1, max_word_len):
                if idx + i > len(s):
                    break

                if s[idx:idx+i] in wordSet:
                    can_word_break = can_word_break or backtracking(idx+i)
            
            memo[idx] = can_word_break
            return can_word_break
        
        return backtracking(0)

# Time: O(n · L²) → effectively O(n) if L is small/constant (= max_word_len)
#   Python slicing of s[a:b] will take O(b-a) time because it copies over the string
#
# Space: O(n)


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]
