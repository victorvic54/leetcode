# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def max_depth(root):
            if root == None:
                return 0
            
            max_left = 0
            max_right = 0
            if root.left:
                max_left = 1 + max_depth(root.left)
            if root.right:
                max_right = 1 + max_depth(root.right)
            
            self.max_diameter = max(self.max_diameter, max_left + max_right)
            return max(max_left, max_right)
        
        max_depth(root)
        return self.max_diameter

# N = number of nodes
# Time: O(N)
# Space: O(N) (skewed)
#        O(log N) (balanced)
