def find_nb(m):
    if m < 0:
        return -1
    
    n = current_volume = 0
    
    while current_volume < m:
        n += 1
        current_volume += n * n * n

    return n if current_volume == m else -1


#Solução do problema utilizando uma abordagem matemática, tornando mais performático com númeoros muito grandes

import math

def find_nb(m):
    s = math.isqrt(m)
    if s * s == m:
        d = 1 + 8 * s
        s_d = math.isqrt(d)
        if s_d * s_d == d:
            n = (-1 + s_d) // 2
            return n
        else:
            return -1
    else:
        return -1