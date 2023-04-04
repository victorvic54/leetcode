class Solution:
    def partitionString(self, s: str) -> int:
        used_set = set()
        result = 0

        for letter in s:
            if letter not in used_set:
                used_set.add(letter)
                continue
            
            used_set = set(letter)
            result += 1
        
        if len(used_set) != 0:
            result += 1
        
        return result
