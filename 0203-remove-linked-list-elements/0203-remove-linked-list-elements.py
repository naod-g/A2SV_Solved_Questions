# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()

        curr = head
        dp = dummy

        while curr:
            if curr.val != val:
                dp.next = curr
                dp = dp.next
            curr = curr.next
        dp.next = None

        return dummy.next

