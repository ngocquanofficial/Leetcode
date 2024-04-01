# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        slow = head
        fast = head
        for i in range(n) :
            fast = fast.next

        # Base case
        if fast == None :
            head = head.next
            return head

        while True :
            fast = fast.next
            if fast == None :

                slow.next = slow.next.next
                return head
            
            slow = slow.next 
            

            
        