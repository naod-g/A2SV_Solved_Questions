# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        res = []
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        nums[:] = nums[::-1]
        
        for num in nums:
            if not res or res[-1] <= num:
                res.append(num)
        res[:] = res[::-1]

        a = ListNode(res[0])
        curr = a
        for i in range(1, len(res)):
            new_node = ListNode(res[i])
            curr.next = new_node
            curr = curr.next

        return a