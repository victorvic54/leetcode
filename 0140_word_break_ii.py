class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        all_sentences = []
        word_list = set(wordDict)
        def backtracking(i, tmp_sentence):
            if i >= len(s):
                all_sentences.append(" ".join(tmp_sentence))
                return
            
            next_word = s[i:]
            for word in word_list:
                if next_word.startswith(word):
                    backtracking(i + len(word), tmp_sentence + [word])
        backtracking(0, [])
        return all_sentences
