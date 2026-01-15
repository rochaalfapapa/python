def paperwork(n: int, m: int) -> int:
    return max(0, n * m)


#Solução com Guard Clause
def paperwork(n: int, m: int) -> int:
    if min(n, m) < 0:
        return 0
    return n * m