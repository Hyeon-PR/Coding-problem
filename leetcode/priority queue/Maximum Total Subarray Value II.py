import heapq
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 1. Build a Sparse Table for O(1) Range Maximum & Minimum Queries
        # This acts as our optimized lookup instead of a heavy Segment Tree
        K = n.bit_length()
        st_max = [[0] * K for _ in range(n)]
        st_min = [[0] * K for _ in range(n)]

        for i in range(n):
            st_max[i][0] = (nums[i], i)
            st_min[i][0] = (nums[i], i)

        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                # Store both the value and the index of the extreme elements
                left_max, left_max_idx = st_max[i][j - 1]
                right_max, right_max_idx = st_max[i + (1 << (j - 1))][j - 1]
                st_max[i][j] = (
                    (left_max, left_max_idx)
                    if left_max >= right_max
                    else (right_max, right_max_idx)
                )

                left_min, left_min_idx = st_min[i][j - 1]
                right_min, right_min_idx = st_min[i + (1 << (j - 1))][j - 1]
                st_min[i][j] = (
                    (left_min, left_min_idx)
                    if left_min <= right_min
                    else (right_min, right_min_idx)
                )

        def query_max(L: int, R: int):
            j = (R - L + 1).bit_length() - 1
            left, left_idx = st_max[L][j]
            right, right_idx = st_max[R - (1 << j) + 1][j]
            return (left, left_idx) if left >= right else (right, right_idx)

        def query_min(L: int, R: int):
            j = (R - L + 1).bit_length() - 1
            left, left_idx = st_min[L][j]
            right, right_idx = st_min[R - (1 << j) + 1][j]
            return (left, left_idx) if left <= right else (right, right_idx)

        # 2. Max-Heap to track the optimal subarrays tracking across divisions
        # Element format: (-value, L, R, max_idx, min_idx)
        heap = []

        # Seed the heap with the absolute global maximum/minimum range
        if n > 0:
            mx_val, mx_idx = query_max(0, n - 1)
            mn_val, mn_idx = query_min(0, n - 1)
            heapq.heappush(heap, (-(mx_val - mn_val), 0, n - 1))

        # Set to record already processed unique (L, R) boundaries
        visited = {(0, n - 1)}
        total_value = 0

        # 3. Extract the top k distinct subarray values
        for _ in range(k):
            if not heap:
                break
            neg_val, L, R = heapq.heappop(heap)
            total_value += -neg_val

            # If the window can shrink, generate adjacent sub-segments
            if L < R:
                # Candidate 1: Shrink from Left
                if (L + 1, R) not in visited:
                    visited.add((L + 1, R))
                    mx, _ = query_max(L + 1, R)
                    mn, _ = query_min(L + 1, R)
                    heapq.heappush(heap, (-(mx - mn), L + 1, R))

                # Candidate 2: Shrink from Right
                if (L, R - 1) not in visited:
                    visited.add((L, R - 1))
                    mx, _ = query_max(L, R - 1)
                    mn, _ = query_min(L, R - 1)
                    heapq.heappush(heap, (-(mx - mn), L, R - 1))

        return total_value
