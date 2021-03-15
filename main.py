import math
import random
from math import gcd
from collections import namedtuple

# # # входные данные
# def quick_power_alg(x,d,n):
#
#     # x^d(mod n)
#     y = 1
#     while d > 0:
#         if d % 2 == 1:
#             y = (y*x) % n
#         else:
#             d = d // 2
#             x = (x*x) % n
#
#     print(y)
#
# quick_power_alg(595, 703, 991)

# b = pow(595, 703, 991)
# print(b)
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



#############################################################################################################################
# # Task 1
# Программно реализовать процедуру генерации открытого и
# закрытого ключей заданной длины L (128, 256, 512). В качестве открытой экспоненты использовать одно из чисел Ферма (17, 257, 65537). Сформированные
# ключи сохранить в файлы: открытый – в файл public.txt, а закрытый – в файл
# private.txt.

# L = 60, e = 17

# def primFerma(a,n):
#     if a**(n-1)%n==1:
#         print("правдоподобно простое")
#     else:
#         print ("составное")
# primFerma(10,11000101)

# def is_prime(num, test_count):
#     for i in range(test_count):
#
#         rnd = random.randint(1, num - 1)
#
#         if (rnd ** (num - 1) % num != 1):
#             return False
#
#     return True

# def toBinary(n):
#     r = []
#     while (n > 0):
#         r.append(n % 2)
#         n = n / 2
#         return r


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
    print("d: " + str(d))
    print("s: " + str(s))
    print("t: " + str(t))
    return s

def is_Prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True

def rand_prostoy_chislo(numeric, temp):
    result = random.getrandbits(numeric)
    # print("1: " + str(result))
    while result % 2 == 0:
        if result % 2 == 0:
            result = random.getrandbits(numeric)
    # print("2: " + str(result))
    b = is_Prime(result)
    # print(b)

    if b == True:
        print(result)
        print("True")

        if temp == 1:
            with open("p_prime.txt", mode='w', encoding="utf-8") as file_p:
                file_p.write(str(result))
        elif temp == 2:
            with open("q_prime.txt", mode='w', encoding="utf-8") as file_q:
                file_q.write(str(result))

        return result
    else:
        rand_prostoy_chislo(numeric, temp)

# def phi(n): # функция Эйлера
#     amount = 0
#     for k in range(1, n + 1):
#         if gcd(n, k) == 1:
#             amount += 1
#     return amount
def phi(p,q):
    phi_n = ((p-1)*(q-1))
    return phi_n

def find_e(f):
    if gcd(f,17) == 1:
        return 17
    elif gcd(f,257) == 1:
        return 257
    elif gcd(f, 65537) == 1:
        return 65537
    else:
        return False

def key_gen(l):
    # l = 512  # key lengh
    print("Генерируем числа p и q заданной битовой длины и проверяем на простоты тестом Миллера-Рабина: ")
    l_half = l//2
    print("p is: ")
    prime_p = rand_prostoy_chislo(l_half, 1)
    print("q is: ")
    prime_q = rand_prostoy_chislo(l_half, 2)
    with open('p_prime.txt') as p:  # считываем регистр
        p = p.read()
    with open('q_prime.txt') as q:  # считываем регистр
        q = q.read()
    p = int(p)
    q = int(q)
    print("Вычисляем n: ")
    n = p*q
    print("n is: " + str(n))
    print("Вычисляем функцию Эйлера: ")
    f = phi(p, q)
    print("phi_n: " + str(f))
    print("Вычисляем открытую экспоненту: ")
    e = find_e(f)
    print("e is: " + str(e))
    print("Вычисляем открытый ключ: ")
    print("open key (e,n) is: " + str(e) + ", " + str (n))
    with open("public.txt", mode='w', encoding="utf-8") as key_pub:
        key_pub.write(str(e) + ", " + str(n))

    # найдем закрытый ключ расширенным алгоритмом евклида
    # входные данные: m = e, n = f
    # выходные данные: s = d, if s < 0: s=s+f
    print("Расширенный алгоритм Евклида для нахождения закрытой экспоненты (e*d)mod фи(n) = 1: ")
    d = Evklid_alg_extended(e,f) # закрытая экспонента
    # print(d)
    if d < 0:  # если d меньше 0, прибавляем фи
        d = d + f
    # print(d)
    print("Вычисляем закрытый ключ: ")
    print("private key (d,n) is: " + str(d) + ", " + str (n))
    with open("private.txt", mode='w', encoding="utf-8") as key_priv:
        key_priv.write(str(d) + ", " + str(n))


def RSA_encryption():
    return 0


def RSA_decryption():
    return 0


if __name__ == '__main__':
    key = key_gen(512) # находит n
    # необхоимо релизовать нахождение функции Эйлера (phi)
    # e = 257 - открытая экспонента, взаимно простая с phi(n)
    # (e,n) - открытый ключ
    # (e*d) mod phi(n) - вычисляем d расшир алг Евклида

