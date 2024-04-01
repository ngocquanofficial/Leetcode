# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while True :
            if not fast :
                return None
            if not fast.next :
                return None
            
            slow = slow.next

            fast = fast.next.next
            
            if slow == fast :
                # First meeting
                first_meeting = fast
                break
        
        # We can make sure that there is a cycle
        fast = head
        slow = first_meeting
        # slow move from first_meeting

        while True :
            if fast == slow :
                return fast
            slow = slow.next
            fast = fast.next

            
