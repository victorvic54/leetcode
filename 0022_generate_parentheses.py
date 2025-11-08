class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def backtracking(left, right, stack):
            if left == 0 and right == 0:
                results.append("".join(stack))
                return
            
            if len(stack) == 0:
                if left > 0:
                    backtracking(left - 1, right, stack + ["("])
            else:
                if left > 0:
                    backtracking(left - 1, right, stack + ["("])
                if right > 0 and right > left:
                    backtracking(left, right - 1, stack + [")"])
        
        backtracking(n, n, [])
        return results

"""
Time: Cₙ = (1 / (n + 1)) * (2n choose n)
Time: O(4ⁿ / √n)

Space:
Recursion depth: at most 2n, so call stack uses O(n) space.
Output storage: there are Cₙ valid strings, each of length 2n.
That’s O(Cₙ × n) to store all results.
"""
