class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def backtracking(idx1, idx2):
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            if idx1 >= len(s1) and idx2 >= len(s2):
                return 0
            
            total_delete = 0
            if idx1 < len(s1) and idx2 >= len(s2):
                total_delete += ord(s1[idx1]) + backtracking(idx1 + 1, idx2)
            
            if idx1 >= len(s1) and idx2 < len(s2):
                total_delete += ord(s2[idx2]) + backtracking(idx1, idx2 + 1)
            
            if not (idx1 < len(s1) and idx2 < len(s2)):
                memo[(idx1, idx2)] = total_delete
                return total_delete
            
            if s1[idx1] == s2[idx2]:
                total_delete += backtracking(idx1 + 1, idx2 + 1)
            else:
                total_delete += min(
                    ord(s1[idx1]) + backtracking(idx1 + 1, idx2),
                    ord(s2[idx2]) + backtracking(idx1, idx2 + 1),
                )
            memo[(idx1, idx2)] = total_delete
            return total_delete
        
        return backtracking(0, 0)

# Time: O(len(s1)*len(s2))
# Space: O(len(s1)*len(s2))
