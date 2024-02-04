class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        for i in range(0 + k, len(word), k):
            if word.startswith(word[i:]):
                return i // k
        
        return math.ceil(len(word) / k)

