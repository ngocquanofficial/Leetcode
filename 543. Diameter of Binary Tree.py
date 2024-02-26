# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def max_depth(self, root):
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        current_diameter = left_depth + right_depth
        if current_diameter > self.max_diameter:
            self.max_diameter = current_diameter
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root):
        max_diameter = 0
        self.max_depth(root)
        return self.max_diameter
