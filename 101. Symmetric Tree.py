# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        left = root.left
        right = root.right
        return self.symmetric_node(left, right)

    def symmetric_node(self, left, right) :
        # Base case
        if left == None :
            return right == None # Then left, right must be None
        if right == None : # and left != None 
            return False
        if left.val != right.val : # First check
            return False
        
# When left, right not None

        # Base case, for symmetric leaves of tree
        # if left.left == None and left.right == None :
        #     return (right.left == None) and (right.right == None)
        
        # if left.left == None : # And left.right != None :
        #     return (right.right == None) and self.symmetric_node(left.right, right.left)

        # if left.right == None :
        #     return (right.left == None) and self.symmetric_node(left.left, right.right)
        return self.symmetric_node(left.left, right.right) and self.symmetric_node(left.right, right.left)
