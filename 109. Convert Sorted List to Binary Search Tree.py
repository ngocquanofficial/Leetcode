# Definition for singly-linked list.
# From NgocQuan with love
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# When submit, don not forget to hide code before this line
class Solution:
    def get_middle(self, head) :
        fast = head
        slow = head
        prev = None
        while fast and fast.next :
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev  :
            prev.next = None
        return slow
    def sortedListToBST(self, head): 
        if head is None :
            return None
        if head.next is None :
            return TreeNode(val= head.val)
        
        middle = self.get_middle(head)
        root = TreeNode(val= middle.val)
        root.right = self.sortedListToBST(middle.next)
        middle.next = None
        root.left = self.sortedListToBST(head)
        return root

            
        
        