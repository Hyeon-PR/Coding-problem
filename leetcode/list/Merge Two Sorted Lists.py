# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        merged = None
        while list1 and list2:
            if list1.val > list2.val:
                if merged:
                    cur.next = list2
                    cur = cur.next
                else:
                    merged = list2
                    cur = list2
                list2 = list2.next
            else:
                if merged:
                    cur.next = list1
                    cur = cur.next
                else:
                    merged = list1
                    cur = list1
                list1 = list1.next
        if list1:
            if merged:
                cur.next = list1
            else:
                merged = list1
        elif list2:
            if merged:
                cur.next = list2
            else:
                merged = list2
        return merged


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 둘 중 남아있는 리스트를 O(1)로 바로 연결
        cur.next = list1 if list1 else list2

        return dummy.next
