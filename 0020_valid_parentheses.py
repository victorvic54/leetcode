class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                continue
            
            if len(stack) == 0:
                return False

            if char == ")" and stack.pop() != "(":
                return False
            
            if char == "}" and stack.pop() != "{":
                return False

            if char == "]" and stack.pop() != "[":
                return False
        
        return len(stack) == 0

# Time: O(n)
# Space: O(n)
