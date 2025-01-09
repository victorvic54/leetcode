class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_length = len(pref)

        result = 0
        for word in words:
            if len(word) >= pref_length and word[0:pref_length] == pref:
                result += 1
        
        return result
