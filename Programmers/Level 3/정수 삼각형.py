def solution(triangle):
    dp = [[0] * len(triangle[-1]) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle) - 1):
        for k in range(i + 1):
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][k] + triangle[i + 1][k])
            dp[i + 1][k + 1] = max(dp[i + 1][k + 1], dp[i][k] + triangle[i + 1][k + 1])

    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))