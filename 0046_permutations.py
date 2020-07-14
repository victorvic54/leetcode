class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtracking(tmp_list):
            if (len(tmp_list) == len(nums)):
                result.append(tmp_list.copy())
            else:
                for i in range(len(nums)):
                    if (nums[i] in tmp_list):
                        continue
                    
                    tmp_list.append(nums[i])
                    backtracking(tmp_list)
                    tmp_list.pop()
        
        backtracking([])
        return result