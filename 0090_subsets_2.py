class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        is_used = [False] * len(nums)
        
        def backtracking(start, tmp_list):
            result.append(tmp_list.copy())
            
            for i in range(start, len(nums)):
                if (i > 0 and not is_used[i-1] and nums[i-1] == nums[i]):
                    continue

                is_used[i] = True
                backtracking(i + 1, tmp_list + [nums[i]])
                is_used[i] = False
        
        backtracking(0, [])
        return result