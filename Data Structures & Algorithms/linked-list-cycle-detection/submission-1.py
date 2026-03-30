# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        
        return False

        # nodes = []
        # while head:
        #     nodes.append(head)
        #     print(nodes)
        #     if (head.next in nodes):
        #         return True
        #     head = head.next
        # return False