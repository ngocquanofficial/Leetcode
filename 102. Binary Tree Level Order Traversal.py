# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []

        queue = []
        visited = set()
        step = 0

        queue.append(root)
        if root == None :
            return []

        while len(queue) > 0 :
            curr_layer = []
            for i in range(len(queue)) :
                curr_node = queue.pop(0)
                curr_layer.append(curr_node.val)
                adjacent = [curr_node.left, curr_node.right]
                for adj_node in adjacent :
                    if adj_node != None :
                        queue.append(adj_node)
                
            ans.append(curr_layer)

        return ans

