import math
import random
# # # входные данные
# def quick_power_alg(x,d,n):
#
#     # x^d(mod n)
#     y = 1
#     while d > 0:
#         if d % 2 == 1:
#             y = (y*x) % n
#         elif d == d // 2:
#             x = (x * x) % n
#             break
#     print(y)
#
# quick_power_alg(2, 8, 256)


# def fastExp(b, n):
# #     def even(n):#проверка четности
# #         if n % 2 == 0:
# #             return 1
# #         return 0
# #     if n == 0:
# #         return 1
# #     if even(n):
# #         return fastExp(b, n/2)**2
# #     return b*fastExp(b, n-1)
# #
# # print(fastExp(2,8))

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

# # Расширенный алгоритм Евклида
# # найти d=НОД(m,n) и найти s, t такие, что d = s*m + t*n
# def Evklid_alg_extended(m,n):
#     a = m
#     b = n
#     u1 = 1
#     u2 = 0
#     v1 = 0
#     v2 = 1
#     while b != 0:
#         q = a // b
#         r = a % b
#         a = b
#         b = r
#         r = u2
#         u2 = u1 - q*u2
#         u1 = r
#         r = v2
#         v2 = v1 - q*v2
#         v1 = r
#     d = a
#     s = u1
#     t = v1
#     print(d,s,t)
# Evklid_alg_extended(30,18)

#############################################################################################################################
# # Task 1
# Программно реализовать процедуру генерации открытого и
# закрытого ключей заданной длины L (128, 256, 512). В качестве открытой экспоненты использовать одно из чисел Ферма (17, 257, 65537). Сформированные
# ключи сохранить в файлы: открытый – в файл public.txt, а закрытый – в файл
# private.txt.

# L = 60, e = 17

def primFerma(a,n):
    if a**(n-1)%n==1:
        print("правдоподобно простое")
    else:
        print ("составное")
# def rand_prostoy_chislo(numeric):
#     result = []
#     for i in range(numeric):
#         result.append(random.randint(0,1))
#     # if result[numeric-1] == 0:
#     #     rand_prostoy_chislo(numeric)
#     x = len(result) - 1
#     res_perevod = 0
#     for i,v in enumerate(result):
#         res_perevod += v * 10 ** (x-i)
#     with open("prostoy.txt", mode='w', encoding="utf-8") as file_res:
#         file_res.write(str(res_perevod))
#
# rand_prostoy_chislo(10)

def rand_chislo_prime(numeric):
    with open("prostoy.txt", mode="w") as file:
        #bitString = ''.join(random.choice('01') for i in range(numeric-1))
        chislo = []
        chislo = (random.choice('01') for i in range(numeric-1))
        #chislo.append(1)
        file.write(chislo)
rand_chislo_prime(10)
def Open_key():
    l = 60

    return 0


def Private_key():

    return 0

