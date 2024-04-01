# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return None
        if not head.next :
            return head
        pointer = head.next

        while pointer :
            temp = pointer.next

            pointer.next = head
            head = pointer
            pointer = temp

        return head

node5 = ListNode(val=5)
node4 = ListNode(val=4, next= node5)
node3 = ListNode(val=3, next= node4)
node2 = ListNode(val=2, next= node3)
node1 = ListNode(val= 1, next= node2)

obj = Solution()
print(obj.reverseList(node1))
