# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        curr = head
        while curr:
            k += 1
            curr = curr.next

        if k == 1:
            return None
        if k == n:
            return head.next

        curr = head
        for i in range(1, k-n):
            curr = curr.next
            
        curr.next = curr.next.next  if curr.next else None

        return head
