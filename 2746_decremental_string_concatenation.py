class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        self.memo = {}
        self.words = words

        if len(words) == 1:
            return len(words[0])

        return self.backtracking(1, "")
        

    def backtracking(self, cursor, tmp_words):
        if cursor > len(self.words):
            return 0
        
        if tmp_words != "" and (cursor, tmp_words[0], tmp_words[-1]) in self.memo:
            return self.memo[(cursor, tmp_words[0], tmp_words[-1])]
    
        final_length = float('inf')
        if tmp_words == "" or tmp_words[-1] != self.words[cursor-1][0]:
            combined_words = tmp_words + self.words[cursor-1]
            tmp_length = len(self.words[cursor-1])
        else:
            combined_words = tmp_words + self.words[cursor-1][1:]
            tmp_length = len(self.words[cursor-1]) - 1

        final_length = min(final_length, tmp_length + self.backtracking(cursor + 1, combined_words))
        
        if tmp_words == "" or self.words[cursor-1][-1] != tmp_words[0]:
            combined_words = self.words[cursor-1] + tmp_words
            tmp_length = len(self.words[cursor-1])
        else:
            combined_words = self.words[cursor-1] + tmp_words[1:]
            tmp_length = len(self.words[cursor-1]) - 1
        
        final_length = min(final_length, tmp_length + self.backtracking(cursor + 1, combined_words))
        
        if tmp_words != "":
            self.memo[(cursor, tmp_words[0], tmp_words[-1])] = final_length

        return final_length
