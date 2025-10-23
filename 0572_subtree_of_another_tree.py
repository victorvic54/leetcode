from typing import Optional, List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Serialize tree as PREORDER with null sentinels so structure is preserved.
    def getListFromTree(self, tree_node: Optional['TreeNode']) -> List[object]:
        out = []
        def dfs(node):
            if node is None:
                out.append(None)  # sentinel
                return
            out.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(tree_node)
        return out

    def isSubtree(self, root: Optional['TreeNode'], subRoot: Optional['TreeNode']) -> bool:
        # Edge cases
        if subRoot is None:
            return True

        if root is None:
            return False

        text  = self.getListFromTree(root)      # big sequence
        pat   = self.getListFromTree(subRoot)   # pattern sequence

        # Build LPS (Longest Prefix Suffix) table for pattern
        lps = [0] * len(pat)
        j = 0
        for i in range(1, len(pat)):
            while j > 0 and pat[i] != pat[j]:
                j = lps[j - 1]
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j

        # KMP search: does pat occur in text?
        j = 0
        for i in range(len(text)):
            while j > 0 and text[i] != pat[j]:
                j = lps[j - 1]
            if text[i] == pat[j]:
                j += 1
                if j == len(pat):
                    return True
        return False

# Time:
# N = number of nodes in root
# M = number of nodes in subRoot
#
# 1) Tree serialization = O(M + N)
# 2) LPS = O(M)
# 3) KMP = O(N)
#
# Space: O(M + N)
