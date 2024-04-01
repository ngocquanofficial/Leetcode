# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) :
        step_a = 0
        step_b = 0
        len_a = -1
        len_b = -1
        pointer_a = headA
        pointer_b = headB
        while True :
            if pointer_a == None :
                len_a = step_a
                break
            pointer_a = pointer_a.next
            step_a += 1

        while True :
            if pointer_b == None :
                len_b = step_b
                break
            pointer_b = pointer_b.next
            step_b += 1

        diff = step_a - step_b
        if diff > 0 :
            for i in range(diff) :
                headA = headA.next
        elif diff < 0 :
            for i in range(-diff) :
                headB = headB.next

        while True :
            if headA == None or headB == None :
                return None
            
            if headA == headB :
                return headA
            
            headA = headA.next
            headB = headB.next
        
                
            