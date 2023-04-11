class Solution:
    def removeStars(self, s: str) -> str:
        word_list = []

        for char in s:
            if char == "*":
                word_list.pop()
            else:
                word_list.append(char)
        
        return "".join(word_list)
