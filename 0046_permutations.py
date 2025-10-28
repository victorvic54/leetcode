class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtracking(arr):
            if len(arr) == len(nums):
                result.append(arr[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                arr.append(nums[i])
                backtracking(arr)
                arr.pop()
                used[i] = False

        backtracking([])
        return result

"""
Time:
| Component            | Complexity | Explanation                             |
| -------------------- | ---------- | --------------------------------------- |
| Recursion stack      | O(n)       | Depth of recursion = number of elements |
| `arr` path list      | O(n)       | Stores one current permutation path     |
| `used` boolean array | O(n)       | Marks which elements are in use         |
| Result storage       | O(n × n!)  | Stores all permutations                 |

Space:
| Aspect                     | Complexity | Notes                                         |
| -------------------------- | ---------- | --------------------------------------------- |
| Time                       | O(n × n!)  | Each of n! permutations built and copied once |
| Auxiliary space            | O(n)       | Stack + path + used array                     |
| Total space (with results) | O(n × n!)  | Dominated by stored permutations              |
"""
