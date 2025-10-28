class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        num_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def backtracking(idx, arr):
            if len(arr) == len(digits):
                result.append(arr[:])
                return
            
            for char in num_to_chars[digits[idx]]:
                arr.append(char)
                backtracking(idx + 1, arr)
                arr.pop()
        
        backtracking(0, [])
        return ["".join(ls) for ls in result]

"""
with k = 3.5
| Aspect        | Complexity | Notes                                    |
| ------------- | ---------- | ---------------------------------------- |
| Time          | O(n · kⁿ)  | Each of kⁿ combinations built and copied |
| Space (aux)   | O(n)       | Stack + current path                     |
| Space (total) | O(n · kⁿ)  | Includes all strings in result           |
"""
