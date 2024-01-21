class Solution:
    def minimumPushes(self, word: str) -> int:
        word_list = defaultdict(int)
        for letter in word:
            word_list[letter] += 1
            
        word_zip = []
        for word in word_list:
            word_zip.append((word, word_list[word]))
        
        word_zip.sort(key=lambda x: x[1], reverse=True)
        
        ans = 0
        for i in range(0, len(word_zip)):
            _, occurences = word_zip[i]
            ans += occurences * math.ceil((i + 1) / 8)
        
        return ans

