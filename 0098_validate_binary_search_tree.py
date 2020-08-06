# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Two-pass straight forward in order traversal
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        
        def inorder_traversal(node):
            if (not node):
                return
            
            inorder_traversal(node.left)
            result.append(node.val)
            inorder_traversal(node.right)
            
        inorder_traversal(root)
        
        for i in range(1, len(result)):
            if (result[i-1] >= result[i]):
                return False
            
        return True

    # One pass in order traversal
    # Since we know in order traversal result a sorted array, and res is the one that
    # contain the last visited node value, it should be smaller than the next visited node val
    def isValidBST(self, root: TreeNode) -> bool:
        stack, res = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return True
            
            node = stack.pop()
            # res stores the current values in in-order traversal order,
            # node.val should larger than the last element in res
            if res and node.val <= res[-1]:
                return False
            
            res.append(node.val)
            root = node.right