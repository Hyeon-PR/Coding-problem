# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        res = [[]]
        dq = deque()
        dq.append((root, 0))
        while dq:
            cur, cur_l = dq.popleft()
            res[cur_l].append(cur.val)

            if (cur.left or cur.right) and len(res) - 1 == cur_l:
                res.append([])

            if cur.left:
                dq.append((cur.left, cur_l + 1))
            if cur.right:
                dq.append((cur.right, cur_l + 1))
        return res
