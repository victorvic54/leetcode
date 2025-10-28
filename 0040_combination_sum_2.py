class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracking(idx, curr_sum, arr):
            if curr_sum == target:
                result.append(arr)
                return

            if idx >= len(candidates) or curr_sum > target:
                return

            # take
            backtracking(idx + 1, curr_sum + candidates[idx], arr + [candidates[idx]])
   
            # don't take
            j = idx + 1
            while j < len(candidates) and candidates[j] == candidates[idx]:
                j += 1
            backtracking(j, curr_sum, arr)
            return

        backtracking(0, 0, [])
        return result

"""
Time: O(n · 2ⁿ)
Space: O(K × n), where K = number of valid combinations found
"""
