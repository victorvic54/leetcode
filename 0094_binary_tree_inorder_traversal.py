# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        def backtracking(tmp_root):
            if tmp_root:
                backtracking(tmp_root.left)
                result.append(tmp_root.val)
                backtracking(tmp_root.right)
                
        backtracking(root)
        return result
    
    # iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return result
            
            node = stack.pop()
            result.append(node.val)
            root = node.right