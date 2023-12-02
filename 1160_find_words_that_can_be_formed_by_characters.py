from collections import defaultdict

class Solution:
    def canCover(self, targetDict, currDict):
        for key, value in currDict.items():
            if targetDict[key] < value:
                return False
        
        return True
                    
    def countCharacters(self, words: List[str], chars: str) -> int:
        targetDict = defaultdict(int)
        for char in chars:
            targetDict[char] += 1

        result = 0
        for word in words:
            tmpDict = defaultdict(int)
            for char in word:
                tmpDict[char] += 1
            
            if self.canCover(targetDict, tmpDict):
                result += len(word)

        return result
