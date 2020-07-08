class Solution:
    def isValid(self, s: str) -> bool:
        stack_ls = []
        
        for i in s:
            if (i == "{" or i == "[" or i == "("):
                stack_ls.append(i)
            else:
                expected = ""
                
                if (i == "}"):
                    expected = "{"
                elif (i == "]"):
                    expected = "["
                elif (i == ")"):
                    expected = "("
                
                if (stack_ls == []) or (expected != stack_ls.pop()):
                    return False
                
        return stack_ls == []
            