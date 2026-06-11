from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node: int) -> int:
            dq = deque()
            dq.append((node, 0))
            visited[node] = True
            while dq:
                cur, cur_lev = dq.popleft()
                for nxt in graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        dq.append((nxt, cur_lev + 1))
            return cur_lev

        depth = bfs(1)
        return pow(2, depth - 1, 10_000_000_07)
