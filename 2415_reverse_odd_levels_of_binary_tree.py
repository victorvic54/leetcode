# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        while queue:
            tmp_queues = deque([])
            tmp_values = []

            while queue:
                head = queue.popleft()
                if head.left:
                    tmp_queues.append(head.left)
                    tmp_values.append(head.left.val)
                if head.right:
                    tmp_queues.append(head.right)
                    tmp_values.append(head.right.val)
            
            if (level + 1) % 2 == 1:
                tmp_values = tmp_values[::-1]
            
            for i in range(len(tmp_queues)):
                tmp_queues[i].val = tmp_values[i]
            
            level += 1
            queue = tmp_queues

        return root

