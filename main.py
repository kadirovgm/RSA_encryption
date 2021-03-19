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

def toBinary(a):
    result = []

    while a:
        result.append(a % 2)
        a //= 2
    result.reverse()
    return result


# Расширенный алгоритм Евклида (-1 1)
# найти d=НОД(m,n) и найти s, t такие, что d = s*m + t*n
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


def is_Prime(n):

    if n != int(n): # проверка на целостность
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9: # проверка случаев при которых false
        return False

    if n == 2 or n == 3 or n == 5 or n == 7: # проверка вариантов при которых true
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1  # битовый сдвиг на след степень двойки
        s += 1
    assert (2 ** s * d == n - 1)  # инструкция проверки условия

    def trial_composite(a):  # проверка на составное число
        if pow(a, d, n) == 1:  # a^d mod(n)
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n) # случ от 2 до n
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
def phi(p, q):
    phi_n = ((p - 1) * (q - 1))
    return phi_n


def find_e(f):
    if gcd(f, 17) == 1:
        return 17
    elif gcd(f, 257) == 1:
        return 257
    elif gcd(f, 65537) == 1:
        return 65537
    else:
        return False


def key_gen(l):
    # l = 512  # key lengh
    print("Генерируем числа p и q заданной битовой длины и проверяем на простоты тестом Миллера-Рабина: ")
    l_half = l // 2
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
    n = p * q
    print("n is: " + str(n))
    print("Вычисляем функцию Эйлера: ")
    f = phi(p, q)
    print("phi_n: " + str(f))
    print("Вычисляем открытую экспоненту: ")
    e = find_e(f)
    print("e is: " + str(e))
    print("Вычисляем открытый ключ: ")
    print("open key (e,n) is: " + str(e) + ", " + str(n))
    with open("public.txt", mode='w', encoding="utf-8") as key_pub:
        key_pub.write(str(e) + ", " + str(n))

    # найдем закрытый ключ расширенным алгоритмом евклида
    # входные данные: m = e, n = f
    # выходные данные: s = d, if s < 0: s=s+f
    print("Расширенный алгоритм Евклида для нахождения закрытой экспоненты (e*d)mod фи(n) = 1: ")
    d = Evklid_alg_extended(e, f)  # закрытая экспонента
    # print(d)
    if d < 0:  # если d меньше 0, прибавляем фи
        d = d + f
    # print(d)
    print("Вычисляем закрытый ключ: ")
    print("private key (d,n) is: " + str(d) + ", " + str(n))
    with open("private.txt", mode='w', encoding="utf-8") as key_priv:
        key_priv.write(str(d) + ", " + str(n))
    return e, n, d


def RSA_encryption(length, e, n):
    print("<Шифрование>")
    # text = random.getrandbits(lengh // 8)
    with open("text.txt") as text_file:
        text = text_file.read()

    text_binary = [format(int.from_bytes(i.encode(), 'big'), '08b') for i in text] # перевод в двоичный код
    text_binary = ''.join(text_binary) # объединение
    text_binary = [text_binary[x:x + length//4] for x in range(0, len(text_binary), length//4)] # разделение на блоки по l//4

    res = []
    for i in text_binary:
        i = int(i, 2)
        res.append(pow(i, e, n)) # шифрование
    res = ' '.join(map(str, res))

    print("Исходное сообщение: " + str(text))
    print("Зашифрованное сообщение: " + str(res))
    text_binary = ' '.join(map(str, text_binary))
    print("Зашифрованное сообщение в бинарном виде: " + str(text_binary))
    with open("encrypted.txt", mode='w', encoding="utf-8") as enc_text:
        enc_text.write(str(text_binary))
    # text = int(text)
    # text_bin = toBinary(text)
    # print("Исходное сообщение в бинарном виде: " + str(text_bin))
    # print(len(text_bin))

    # encrypted = pow(text, e, n)
    # print("pow: " + str(encrypted))
    return res

def RSA_decryption(encrypted, d,n, length):
    print("<Дешифрование>")
    encrypted = encrypted.split(' ') # разделение
    res = []
    for i in encrypted:
        res.append(pow(int(i), d, n)) # дешифрование

    res = [bin(i)[2:].zfill(length//4) for i in res] # дополнение нулями слева

    res_binary = ''.join(map(str, res)) # объединение

    n = int(res_binary, 2)

    decrypted = n.to_bytes((n.bit_length()) + 7//8, 'big') # перевод в int строку двоичную
    decrypted = decrypted.decode()
    print("-----" + str(decrypted))
    decrypted_null = decrypted.replace('NULL', '')


    # decrypted = pow(int(encrypted), d, n)
    print("Расшифрованное сообщение: " + str(decrypted_null))
    with open("decrypted.txt", mode='w') as dec_text:
        dec_text.write(str(decrypted_null))
    return decrypted

#
# def Ro_Pollard(n):
#     x = random.randint(1, n-2)
#     y = 1
#     i = 0
#     stage = 2
#     while gcd(n, abs(x-y) == 1):
#         if i == stage:
#             y = x
#             stage = stage*2
#         x = (x * x + 1) % n
#         i = i + 1
#     return gcd(n, abs(x-y))


if __name__ == '__main__':
    l = 512
    e, n, d = key_gen(l)  # находит n
    # print(e, n, d)
    enc = RSA_encryption(l, e, n)
    dec = RSA_decryption(enc, d, n, l)

    # Написать программу, реализующую атаку на алгоритм RSA
    # (вычисление закрытого ключа по известному открытому ключу) с использованием ρ-эвристики Полларда. Результатом работы программы должно быть разложение заданного числа n на два простых множителя p и q
