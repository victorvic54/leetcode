class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        result = []
        
        def backtracking(start, tmp_list):
            result.append(tmp_list.copy())
            
            for i in range(start, nums_len + 1):
                backtracking(i + 1, tmp_list + [nums[i-1]])
        
        backtracking(1, [])
        return result