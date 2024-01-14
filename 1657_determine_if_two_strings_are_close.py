class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dict = defaultdict(int)
        word2_dict = defaultdict(int)
        for char in word1:
            word1_dict[char] += 1
        
        for char in word2:
            word2_dict[char] += 1
        
        for key in word1_dict:
            if key not in word2_dict:
                return False

        return sorted(word1_dict.values()) == sorted(word2_dict.values())

