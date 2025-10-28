class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(idx, curr_sum, arr):
            if curr_sum == target:
                result.append(arr[:])
                return

            if idx >= len(candidates) or curr_sum > target:
                return
            
            # take
            arr.append(candidates[idx])
            backtracking(idx, curr_sum + candidates[idx], arr)
            arr.pop()

            # don't take
            backtracking(idx + 1, curr_sum, arr)
            return
        
        backtracking(0, 0, [])
        return result

"""
Let:
n = len(candidates)
T = target
m = min(candidates)
You can only go as deep as T / m in the recursion tree
Time: O(2^(T/m))

Recursion depth: O(T/m)
Output storage: depends on how many combinations exist (can also be exponential)
Space: O(T/m) + output size
"""
