class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        n = max(len(word1), len(word2))

        for i in range(n):
            if i < len(word1):
                s.append(word1[i])
            if i < len(word2):
                s.append(word2[i])

        return "".join(s)


class WeirdSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [""] * (len(word1) + len(word2))
        threshold = min(len(word1), len(word2))
        result[:2*threshold:2] = word1[:threshold]
        result[1:2*threshold:2] = word2[:threshold]

        if (len(word1) > len(word2)):
            result[2*threshold:] = word1[threshold:]
        else:
            result[2*threshold:] = word2[threshold:]
        
        return "".join(result)

