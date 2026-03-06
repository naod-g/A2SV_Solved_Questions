# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        odd = head
        even = head.next

        curr = odd
        while curr and curr.next:
            temp = curr.next
            curr.next = curr.next.next

            curr = temp
        
        curr = odd
        while curr.next:
            curr = curr.next

        curr.next = even
        return odd
        
