class Solution:
    def isPalindrome(self, string):
        for i in range(0, len(string) // 2):
            if string[i] != string[len(string)-i-1]:
                return False
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
