# def Evklid_alg(a, b): # делением
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print(a+b)
#
#
# print(Evklid_alg(76151,87391))

def Evklid_alg_extended(m, n):
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
        u2 = u1 - q * u2
        u1 = r
        r = v2
        v2 = v1 - q * v2
        v1 = r
    d = a
    s = u1
    t = v1
    print("d: " + str(d))
    print("s: " + str(s))
    print("t: " + str(t))
    return s

print(Evklid_alg_extended(11,143))