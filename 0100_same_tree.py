# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(tree, tmp_list):
            if (not tree):
                tmp_list.append(None)
            else:
                tmp_list.append(tree.val)
            
                if (tree.left or tree.right):
                    helper(tree.left, tmp_list)
                    helper(tree.right, tmp_list)
                    
            return tmp_list
              
        result_p = helper(p, [])
        result_q = helper(q, [])
        
        return result_p == result_q