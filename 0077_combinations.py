class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtracking(start, tmp_list):
            if (len(tmp_list) == k):
                result.append(tmp_list.copy())
            else:   
                for i in range(start, n + 1):
                    backtracking(i + 1, tmp_list + [i])
        
        backtracking(1, [])
        return result