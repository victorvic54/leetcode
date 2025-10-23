# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def max_depth(root):
            if root == None:
                return 0
            
            max_left = 0
            max_right = 0
            if root.left:
                max_left = 1 + max_depth(root.left)
            if root.right:
                max_right = 1 + max_depth(root.right)
            
            if abs(max_left - max_right) > 1:
                self.is_balanced = False
            
            return max(max_left, max_right)
        
        max_depth(root)
        return self.is_balanced

# N = number of nodes
# Time: O(N)
# Space: O(N) (skewed)
#        O(log N) (balanced)
