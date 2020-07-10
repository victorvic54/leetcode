'''

Things to note:
1. Since the len of the word in the list is the same (consistent) we can apply this method
2. Basically store in the dictionary all the list of word then read for every (word_len * word_list_len) from the string
   Copy the dictionary for every iteration, checked if it is used all te words in dictionary

'''

class Solution:
     def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        
        string_len = len(s)
        word_list_len = len(words)
        word_len = len(words[0])
        
        word_dict = defaultdict(int)
        
        for word in words:
            word_dict[word] += 1
        
        def is_match_word_at(index: int):
            word_dict_copy = word_dict.copy()
            
            for idx in range(word_list_len):
                start = idx * word_len
                end = (idx + 1) * word_len
                string_word = s[index + start : index + end]
                
                if not word_dict_copy[string_word]:
                    return False
                
                word_dict_copy[string_word] -= 1
                
            return True
        
        return [index for index in range(string_len - (word_len * word_list_len) + 1) 
                if is_match_word_at(index)]