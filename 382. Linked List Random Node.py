# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head):
        self.head = head
        self.nodes = []

        
        

    def getRandom(self):
        node = self.head
        length = 0
        # Pre-count the length of nodes, as well as save these node values in a list
        while node :
            self.nodes.append(node.val)
            length += 1
            node = node.next
        return random.choice(self.nodes)

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()