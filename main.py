import math
# входные данные
def quick_power_alg():
    x, d, n = 0
    # x^d(mod n)
    y = 1
    while d > 0:
        if d % 2 == 1:
            y = (y*x) mod n
        elif d == d // 2 or x = (x*x) mod n:
            break
    return y


