# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return
        prev = head
        current = head.next
        head.next = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev
