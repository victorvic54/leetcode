class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtracking(idx, arr):
            result.append(arr)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                backtracking(i + 1, arr + [nums[i]])

        backtracking(0, [])
        return result

"""
Time: O(n · 2ⁿ)
There are up to 2ⁿ subsets; each recursive step may copy up to O(n) when doing arr + [x].
Sorting adds O(n log n) upfront (dominated by the exponential term).

Space (auxiliary): O(n) + O(n · 2ⁿ) = O(n · 2ⁿ)
- Recursion depth and the current path.
- To store all subsets.
"""
