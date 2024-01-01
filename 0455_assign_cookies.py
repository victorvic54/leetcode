# Space Complexity: O(n+m) for .sort() in python because only one of the recursive tree is being process at a time
# n + n/2 + n/4 + ... ->  2n
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_idx = 0
        s_idx = 0

        contented_child = 0
        while g_idx < len(g) and s_idx < len(s):
            if s[s_idx] >= g[g_idx]:
                contented_child += 1
                s_idx += 1
                g_idx += 1
            else:
                s_idx += 1
        
        return contented_child

