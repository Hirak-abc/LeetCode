# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        vals = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        left,right = 0,len(vals)-1

        while left<right:
            current_sum = vals[left] +vals[right]

            if current_sum == k:
                return True
            elif current_sum<k:
                left+=1
            else:
                right-=1
        return False

        