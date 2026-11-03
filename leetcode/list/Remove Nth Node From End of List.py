# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        prev = None
        cur = head
        if cur.next == None:
            return None

        leng = 0
        while cur:
            cur = cur.next
            leng += 1
        cur = head
        for i in range(leng - n):
            prev = cur
            cur = cur.next
        if prev == None:
            return cur.next
        prev.next = cur.next
        return head
