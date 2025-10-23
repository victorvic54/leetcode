# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        max_depth = 0
        max_depth = max(max_depth, 1 + self.maxDepth(root.left))
        max_depth = max(max_depth, 1 + self.maxDepth(root.right))
        return max_depth

# N = number of nodes
# Time: O(N)
# Space: O(N) (skewed)
#        O(log N) (balanced)
