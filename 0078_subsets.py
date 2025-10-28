class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(idx, arr):
            result.append(arr[:])
            for i in range(idx, len(nums)):
                arr.append(nums[i]) # use this way to avoid O(k) copies on every backtracking
                backtracking(i + 1, arr)
                arr.pop()
        
        backtracking(0, [])
        return result

# same time complexity as subsets2 but it is much faster by copy upon getting the solution list


    def subsets2(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(idx, arr):
            result.append(arr)
            for i in range(idx, len(nums)):
                backtracking(i + 1, arr + [nums[i]])
        
        backtracking(0, [])
        return result

# Time: O(n * 2^n)
# Space: O(n * 2^n)
