import math
# # входные данные
# def quick_power_alg():
#     x, d, n = 0
#     # x^d(mod n)
#     y = 1
#     while d > 0:
#         if d % 2 == 1:
#             y = (y*x) mod n
#         elif d == d // 2 or x = (x*x) mod n:
#             break
#     return y


# # Алгоритм Евклида
#
# def Evklid_alg(a, b): # делением
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print(a+b)

# # Алгоритм Евклида вычитанием
#
# def Evklid_alg_minus(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     print(a)
#


# # Алгоритм Евклида по книжке
#
# def Evklid_alg_kniga(a,b):
#     while b != 0:
#         temp = a % b
#         a = b
#         b = temp
#     print(a)
# Evklid_alg_kniga(30,18)

# Расширенный алгоритм Евклида
# найти d=НОД(m,n) и найти s, t такие, что d = s*m + t*n
def Evklid_alg_extended(m,n):
    a = m
    b = n
    u1 = 1
    u2 = 0
    v1 = 0
    v2 = 1
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        r = u2
        u2 = u1 - q*u2
        u1 = r
        r = v2
        v2 = v1 - q*v2
        v1 = r
    d = a
    s = u1
    t = v1
    print(d,s,t)
Evklid_alg_extended(30,18)