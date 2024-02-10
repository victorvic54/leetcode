class Solution:
    def isPalindrome(self, string):
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        palindrome_map = {}

        def backtracking(idx):
            if idx == len(s) - 1:
                return 1

            ans = 0
            for i in range(idx + 1, len(s) + 1):
                if s[idx:i] not in palindrome_map:
                    palindrome_map[s[idx:i]] = self.isPalindrome(s[idx:i])
                if palindrome_map[s[idx:i]]:
                    ans += 1

            ans += backtracking(idx + 1)
            return ans

        return backtracking(0)

