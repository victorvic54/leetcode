class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = set()
        counting_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.add(i)
                counting_stack.append(i)
            elif s[i] == ")":
                if len(counting_stack) != 0:
                    stack.add(i)
                    counting_stack.pop()
        
        for idx in counting_stack:
            stack.remove(idx)
        
        result = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == ")":
                if i in stack:
                    result.append(s[i])
            else:
                result.append(s[i])
        
        return "".join(result)

