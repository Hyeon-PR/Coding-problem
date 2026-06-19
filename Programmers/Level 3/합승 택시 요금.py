def solution(n, s, a, b, fares):
    answer = float('inf')

    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for fare in fares:
        u, v, w = fare
        dist[u][v] = w
        dist[v][u] = w

    for i in range(1, n + 1):
        dist[i][i] = 0

    for K in range(1, n + 1):
        for S in range(1, n + 1):
            for E in range(1, n + 1):
                if dist[S][E] > dist[S][K] + dist[K][E]:
                    dist[S][E] = dist[S][K] + dist[K][E]

    for x in range(1, n + 1):
        cost = dist[s][x] + dist[x][a] + dist[x][b]
        answer = min(answer, cost)
    return answer