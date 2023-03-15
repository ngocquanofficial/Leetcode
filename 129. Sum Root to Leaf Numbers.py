# This challenging problem is a gift to my mom, today is her birthday
# from NgocQuanNE with luv
# Using stack to travel in DFS, save the (node, current path to this node) to a stack

class Solution(object):
    def sumNumbers(self, root):
        total = 0
        stack = []
        stack.append((root, str(root.val)))
        while stack :
            root, path = stack.pop() # travel in DFS for memory efficient
            if not root :
                continue
            if root.left == None and root.right == None :
                total += int(path)
            if root.left :
                stack.append((root.left, path + str(root.left.val)))
            if root.right :
                stack.append((root.right, path+ str(root.right.val)))
        return total