class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtracking(index, total, tmp_list):
            if (total - target > 0):
                return
            elif (total == target):
                result.append(tmp_list.copy())
            else:
                for i in range(index, len(candidates)):
                    if (i > index and candidates[i-1] == candidates[i]):
                        continue
                        
                    tmp_list.append(candidates[i])
                    backtracking(i + 1, total + candidates[i], tmp_list)
                    tmp_list.pop()
                    
        backtracking(0, 0, [])
        return result