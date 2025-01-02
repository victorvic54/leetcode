class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # keep track all of the word that start and ends vowel
        prefix_arr = [0]
        prefix_sum = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum += 1
            prefix_arr.append(prefix_sum)

        vowel_count = []
        for l, r in queries:
            vowel_count.append(prefix_arr[r+1] - prefix_arr[l])
        return vowel_count

