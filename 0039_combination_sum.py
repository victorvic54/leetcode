class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking(index, total, tmp_list):
            if (total - target > 0):
                return
            elif (total == target):
                result.append(tmp_list.copy())
            else:
                for i in range(index, len(candidates)):
                    tmp_list.append(candidates[i])
                    backtracking(i, total + candidates[i], tmp_list)
                    tmp_list.pop()
                    
        backtracking(0, 0, [])
        return result