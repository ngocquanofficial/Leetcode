"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def __init__(self) :
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node :
            return node
        
        if node in self.visited :
            return self.visited[node]

        clone_root = Node(node.val, [])
        self.visited[node] = clone_root
        neighbors = node.neighbors

        clone_root.neighbors = [self.cloneGraph(i) for i in neighbors]
        return clone_root
        
        
