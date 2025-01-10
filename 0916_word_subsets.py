class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combined_dict = Counter()
        for word in words2:
            for char, count in Counter(word).items():
                combined_dict[char] = max(combined_dict[char], count)

        universal_strings = []
        for word in words1:
            word_counter = Counter(word)
            if all(word_counter[char] >= count for char, count in combined_dict.items()):
                universal_strings.append(word)

        return universal_strings

