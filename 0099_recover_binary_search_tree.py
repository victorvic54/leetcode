# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(1) recursive solution
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_error_node = None
        self.second_error_node = None
        self.prev_node = TreeNode(float('-inf'))
        
        def in_order_traversal(tmp_root):
            if (not tmp_root):
                return
            
            in_order_traversal(tmp_root.left)
            
            if (not self.first_error_node and self.prev_node.val >= tmp_root.val):
                self.first_error_node = self.prev_node
                
            if (self.first_error_node and self.prev_node.val >= tmp_root.val):
                self.second_error_node = tmp_root
                
            self.prev_node = tmp_root
            in_order_traversal(tmp_root.right)
        
        in_order_traversal(root)
        self.first_error_node.val, self.second_error_node.val = self.second_error_node.val, self.first_error_node.val


    # O(n) iterative solution
    def recoverTree(self, root):
        stack = []
        prev_node = None
        first_error_node = None
        second_error_node = None
        
        # iterative in order traversal using stack
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                break

            root = stack.pop()

            # first time occurs reversed order
            if prev_node and prev_node.val > root.val:
                if not first_error_node:
                     first_error_node = prev_node
                
                #                                                 prev  root
                # didn't use else: to tackle None problem for (1 -> 3 -> 2 -> 4)
                second_error_node = root

            prev_node = root
            root = root.right
        
        first_error_node.val, second_error_node.val = second_error_node.val, first_error_node.val
