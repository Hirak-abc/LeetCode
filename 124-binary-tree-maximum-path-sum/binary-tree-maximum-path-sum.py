# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = float('-inf')

        def maxGain(node):
            if not node:return 0

            left = max(0,maxGain(node.left))
            right = max(0,maxGain(node.right))

            self.ans = max(self.ans,node.val+left+right)

            return node.val + max(left,right)

        maxGain(root)

        return self.ans

