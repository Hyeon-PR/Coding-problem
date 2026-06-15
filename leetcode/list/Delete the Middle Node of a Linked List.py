# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        total = 0
        node = head
        while node:
            total += 1
            node = node.next

        target_idx = total // 2

        curr = head
        for _ in range(target_idx - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head


# https://velog.io/@darcyu83/Algorithm-4.-Fast-Slow-PointersLinked-List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case Handling
        if not head or not head.next:
            return None

        slow = head
        # Offset 'fast' by skipping ahead. This forces 'slow' to stop
        # exactly one step before the actual middle node.
        fast = head.next.next

        # Traversal: Fast moves 2 steps, Slow moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Execute deletion by bypassing the middle node
        slow.next = slow.next.next

        return head
