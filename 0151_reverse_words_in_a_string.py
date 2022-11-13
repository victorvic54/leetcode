'''
First solution: python string manipulation

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


'''
Second solution: without strip(), split(), join()

Idea is reverse all the string first
Iterate all the reversed string
a) if char != " "  and tmp_word != "" and index before is " "
    => words += (word + " ")
    => word = i

b) if char != " "
    => word = char + word
'''
class Solution:
    def reverseWords(self, s):
        word = ""
        words = ""
        s = s[::-1]
        
        for i, char in enumerate(s):
            if char != " " and word != "" and s[i-1] == " ":
                words += word + " "
                word = char
            elif char != " ":
                word = char + word

        words += word
        return(words)
