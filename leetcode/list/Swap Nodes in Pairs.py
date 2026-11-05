# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        even = head
        odd = even.next if even else None
        prev = dummy
        while even and odd:
            even.next = odd.next
            odd.next = even
            prev.next = odd
            prev = even
            even = even.next
            odd = even.next if even else None

        return dummy.next
