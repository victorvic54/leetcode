class Solution:
    def isInt(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isInt(token):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(num2 + num1)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "*":
                    stack.append(num2 * num1)
                elif token == "/":
                    stack.append(int(num2 / num1))
        return stack.pop()

