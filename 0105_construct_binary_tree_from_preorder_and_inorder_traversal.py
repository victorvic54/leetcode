# Time: O(n)
# Space: O(n)
class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        pre = deque(preorder)

        def helper(left, right):
            if left > right:
                return None

            root_val = pre.popleft()
            root = TreeNode(root_val)

            mid = idx_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)


# O(n^2)
class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        idx = 0
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                idx = i
                break
        
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root

