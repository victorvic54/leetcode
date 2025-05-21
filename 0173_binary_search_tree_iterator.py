# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class BSTIterator:
    def __init__(self, root):
        self.stack = list()
        self.push_all(root)

    # time complexity: O(1)
    def hasNext(self):
        return len(self.stack) > 0

    # time complexity avg: O(1) -> total access n nodes of the trees
    def next(self):
        node = self.stack.pop()
        self.push_all(node.right)
        return node.val
        
    def push_all(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

