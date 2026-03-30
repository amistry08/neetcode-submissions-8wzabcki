# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        carry = 0
        while l1 or l2:
            if l1 and l2:
                add = l1.val + l2.val + carry
                carry = add // 10
                node.next = ListNode(add%10)
                node = node.next

            if not l1 and l2:
                add = carry + l2.val
                carry = add // 10
                node.next = ListNode(add%10)
                node = node.next

            if l1 and not l2:
                add = carry + l1.val
                carry = add // 10
                node.next = ListNode(add%10)
                node = node.next
        
            print(node.val, add, sum)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            node.next = ListNode(carry)

        return dummy.next