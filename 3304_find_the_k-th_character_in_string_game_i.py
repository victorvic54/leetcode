class Solution:
    def kthCharacter(self, k: int) -> str:
        depth = 0
        remaining = k
        while remaining != 1:
            depth += 1
            base = int(log2(remaining - 1))
            remaining = remaining - int(2**base)
        
        depth = depth % 26
        return chr(ord('a') + depth)
