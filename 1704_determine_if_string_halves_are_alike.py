class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left_vowel = 0
        right_vowel = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i in range(len(s)):
            if s[i] in vowels:
                if i >= len(s) // 2:
                    right_vowel += 1
                else:
                    left_vowel += 1
        return left_vowel == right_vowel

