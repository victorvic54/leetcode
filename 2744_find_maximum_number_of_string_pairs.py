iclass Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        tmp_dict = defaultdict(int)
        result = 0
        
        for word in words:
            if tmp_dict[word] == 0:
                tmp_dict[word[::-1]] += 1
            else:
                result += 1
                tmp_dict[word] -= 1

        return result
