def transform_order(s):
    num = 0
    for ch in s:
        num = num * 26 + (ord(ch) - ord('a') + 1)
    return num

def solution(n, bans):
    ban_orders = sorted({transform_order(ban) for ban in bans})
    
    target = n
    for b in ban_orders:
        if b <= target:
            target += 1
        else:
            break
            
    res = []
    while target > 0:
        target -= 1
        res.append(chr(target % 26 + ord('a')))
        target //= 26
        
    return "".join(reversed(res))

if __name__ == "__main__":
    solution(30, ["d", "e", "bb", "aa", "ae"])