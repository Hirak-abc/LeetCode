class Solution(object):
    def isValidBST(self, root):
        """:type root: Optional[TreeNode] :rtype: bool"""
        
        def validate(node, low=float('-inf'), high=float('inf')):
            # Base case: an empty tree/node is valid
            if not node:
                return True
            
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Recursively validate left and right subtrees with updated bounds
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)