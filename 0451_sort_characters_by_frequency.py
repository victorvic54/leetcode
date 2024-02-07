class Solution:
    def expandTuple(self, tup):
        char, freq = tup
        return char * freq

    def frequencySort(self, s: str) -> str:
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        freq_list = []
        for char in freq_map:
            freq_list.append((char, freq_map[char]))
        
        freq_list = sorted(freq_list, key=lambda x: x[1], reverse=True)
        expanded_freq_list = map(self.expandTuple, freq_list)
        return "".join(expanded_freq_list)
