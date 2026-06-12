def solution(cards):
    n = len(cards)
    visited = [False] * n
    cycle_sizes = []

    for i in range(n):
        if visited[i]:
            continue
        
        current = i
        count = 0
        while not visited[current]:
            visited[current] = True
            current = cards[current] - 1  # 1-index conversion
            count += 1
        
        cycle_sizes.append(count)
    cycle_sizes.sort(reverse=True)
    if len(cycle_sizes) < 2:
        return 0
    return cycle_sizes[0] * cycle_sizes[1]

print(solution([8,6,3,7,2,5,1,4]))