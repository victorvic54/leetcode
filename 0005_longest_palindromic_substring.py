class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest_palindrome = ""
        self.max_len = 0

        def expand_palindrome(left, right):
            if left < 0 or right >= len(s) or s[left] != s[right]:
                if right - left - 1 > self.max_len:
                    self.longest_palindrome = s[left+1:right]
                    self.max_len = right - left - 1
                return
            
            expand_palindrome(left - 1, right + 1)

        
        for i in range(len(s)):
            expand_palindrome(i, i)
            expand_palindrome(i, i + 1)

        return self.longest_palindrome

# Time: O(n^2)
# Space: O(1)
