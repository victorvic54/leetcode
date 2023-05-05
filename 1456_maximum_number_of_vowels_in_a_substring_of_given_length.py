class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])

        tmp_length = 0
        for i in range(len(s)):
            if i >= k:
                if s[i-k] in vowel_set:
                    tmp_length -= 1
                
            if s[i] in vowel_set:
                tmp_length += 1

            max_vowel = max(max_vowel, tmp_length)

        return max_vowel
