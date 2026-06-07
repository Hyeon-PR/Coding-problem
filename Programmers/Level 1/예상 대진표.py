def solution(n,a,b):
    answer = 1

    if b < a:
        a, b = b, a
    
    while True:
        if (a % 2 == 1 and b % 2 == 0 and b // 2 == a // 2 + 1):
            break
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1
        answer += 1
    return answer


def solution(n, a, b):
    answer = 0
    # Convert to 0-indexed for cleaner division logic
    a -= 1
    b -= 1
    
    while a != b:
        a //= 2
        b //= 2
        answer += 1
        
    return answer

def solution(n, a, b):
    # (a - 1) ^ (b - 1) finds the differing bits.
    # .bit_length() immediately tells us the height of the subtree where they diverge.
    return ((a - 1) ^ (b - 1)).bit_length()

print(solution(8, 4, 7))