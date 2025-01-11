class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        char_dict = Counter(s)
        min_k = 0
        max_k = len(s)
        for char, count in char_dict.items():
            if count % 2 != 0:
                min_k += 1
        return min_k <= k <= max_k

