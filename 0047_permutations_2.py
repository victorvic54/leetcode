class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        is_used_list = [False] * len(nums)
        
        def backtracking(tmp_list):
            if (len(tmp_list) == len(nums)):
                result.append(tmp_list.copy())
            else:
                for i in range(len(nums)):
                    if (is_used_list[i]):
                        continue
                    
                    if (not is_used_list[i-1] and i > 0 and nums[i-1] == nums[i]):
                        continue
                    
                    is_used_list[i] = True
                    backtracking(tmp_list + [nums[i]])
                    is_used_list[i] = False
                    
        backtracking([])
        return result