# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        
        r = postorder.pop() 
        root = TreeNode(r) 
        i = inorder.index(r) 
        
        root.right = self.buildTree(inorder[i+1:], postorder) 
        root.left = self.buildTree(inorder[:i], postorder) 
        return root
