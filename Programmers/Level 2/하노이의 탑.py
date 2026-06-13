def solution(n):
    answer = []

    # source: 1, auxiliary: 2, target: 3
    def hanoi(disk, src, aux, tgt):
        if disk == 1:
            answer.append([src, tgt])
            return
        
        # Step 1: Move n-1 disks from src to aux
        hanoi(disk - 1, src, tgt, aux)
        
        # Step 2: Move the largest disk from src to tgt
        answer.append([src, tgt])
        
        # Step 3: Move n-1 disks from aux to tgt
        hanoi(disk - 1, aux, src, tgt)

    hanoi(n, 1, 2, 3)
    return answer

print(solution(2))