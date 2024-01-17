class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = defaultdict(int)
        for num in arr:
            occurences[num] += 1
        
        unique_set = set()
        for occurence in occurences.values():
            if occurence in unique_set:
                return False
            unique_set.add(occurence)
        
        return True
