class Solution:
    def minimumLength(self, s: str) -> int:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        
        minimum_len = 0
        for _, count in char_dict.items():
            minimum_len += 1 + (count - 1) % 2
        
        return minimum_len

