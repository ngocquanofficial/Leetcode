# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        return self.valid_root(root)

    def find_min(self, root):
        if root == None:
            return
        while root.left != None:
            root = root.left
        return root.val

    def find_max(self, root):
        if root == None:
            return
        while root.right != None:
            root = root.right
        return root.val

    def valid_root(self, root):
        if root.left == None and root.right == None:
            return True
        if root.left == None:
            bool_condition = root.val < self.find_min(root.right) and self.valid_root(
                root.right
            )
            return bool_condition

        if root.right == None:
            bool_condition = root.val > self.find_max(root.left) and self.valid_root(
                root.left
            )
            return bool_condition

        general_case = (
            root.val > self.find_max(root.left)
            and root.val < self.find_min(root.right)
            and self.valid_root(root.left)
            and self.valid_root(root.right)
        )
        return general_case
