class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = defaultdict(int)
        for word in words:
            for char in word:
                char_count[char] += 1
        
        for key in char_count:
            if char_count[key] % len(words) != 0:
                return False
        
        return True
