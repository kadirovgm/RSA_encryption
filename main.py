import math
import random
from math import gcd
import timeit
from collections import namedtuple


# Функция перевода в двоичное число
def toBinary(a):
    result = []

    while a:
        result.append(a % 2)
        a //= 2
    result.reverse()
    return result


# Расширенный алгоритм Евклида
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


# Тест простоты Миллера-Рабина
def is_Prime(n):

    if n != int(n): # проверка на целостность
        return False
    n = int(n)

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


# Функция генерации простых чисел
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


# Функция нахождения фи(n)
def phi(p, q):
    phi_n = ((p - 1) * (q - 1))
    return phi_n


# Функция нахождения открытой экспоненты
def find_e(f):
    if gcd(f, 17) == 1:
        return 17
    elif gcd(f, 257) == 1:
        return 257
    elif gcd(f, 65537) == 1:
        return 65537
    else:
        return False


# Функция генерации ключей
def key_gen(l):
    # l = 512  # key lengh
    print("Генерируем числа p и q заданной битовой длины и проверяем на простоты тестом Миллера-Рабина: ")
    l_half = l // 2
    r = 0.35
    print("p is: ")
    #prime_p = rand_prostoy_chislo(l_half, 1)
    prime_p = rand_prostoy_chislo(int(r*l), 1)

    print("q is: ")
    #prime_q = rand_prostoy_chislo(l_half, 2)
    prime_q = rand_prostoy_chislo(int((1-r)*l), 2)

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


# Шифрование
def RSA_encryption(length, e, n):
    print("<Шифрование>")
    # text = random.getrandbits(lengh // 8)
    with open("text.txt") as text_file:
        text = text_file.read()

    text_binary = [format(int.from_bytes(i.encode(), 'big'), '08b') for i in text]  # перевод в двоичный код
    text_binary = ''.join(text_binary)  # объединение
    text_binary = [text_binary[x:x + length//4] for x in range(0, len(text_binary), length//4)]  # разделение на блоки по l//4

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

    return res


# Дешифрование
def RSA_decryption(encrypted, d, n, length):
    print("<Дешифрование>")
    encrypted = encrypted.split(' ')  # разделение
    res = []
    for i in encrypted:
        res.append(pow(int(i), d, n))  # дешифрование

    res = [bin(i)[2:].zfill(length // 4) for i in res]  # дополнение нулями слева (перевод в двоичный)

    res_binary = ''.join(map(str, res))  # объединение

    n = int(res_binary, 2)
    decrypted = n.to_bytes((n.bit_length()), 'big')  # перевод в int строку двоичную

    decrypted = decrypted.decode()
    # print("-----" + str(decrypted))
    # decrypted_null = decrypted.replace('NULL', '')
    decrypted.lstrip("0")


    # decrypted = pow(int(encrypted), d, n)
    print("Расшифрованное сообщение: " + str(decrypted))
    with open("decrypted.txt", mode='w') as dec_text:
        dec_text.write(str(decrypted))
    return decrypted


# # функция для вычисления (base^exponent)%modulus
# def modular_pow(base, exponent, modulus):
#     # результат
#     result = 1
#
#     while (exponent > 0):
#
#         # if y is odd, multiply base with result
#         if (exponent & 1):
#             result = (result * base) % modulus
#
#         # exponent = exponent/2
#         exponent = exponent >> 1
#
#         # base = base * base
#         base = (base * base) % modulus
#
#     return result


# вычислим делитель n методом ро эвристики Полларда
def PollardRho(n):
    # для единицы делитель 1
    if (n == 1):
        return n
    # если число четное, один из делителей 2
    if (n % 2 == 0):
        return 2
    x = (random.randint(0, 2) % (n - 2))  # остаток от деления случ числа (0, 2) на (n - 2)
    y = x
    # константа для f(x).
    c = (random.randint(0, 1) % (n - 1))
    # результат (потенциальный делитель)
    d = 1
    # пока простой делитель не будет получен
    # если n простой, return n
    while (d == 1):
        # x(i+1) = f(x(i))
        x = (pow(x, 2, n) + c + n) % n
        # y(i+1) = f(f(y(i)))
        y = (pow(y, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        # проверка НОД у |x-y| и n
        d = math.gcd(abs(x - y), n)
        # Если делитель не найден - заново
        if (d == n):
            return PollardRho(n)
    return d


def RSA_attack(e, n):
    start_timer = timeit.default_timer()

    print("\n\nАтака!")
    print("Открытый ключ (e,n): " + str(e) + ", " + str(n))
    print("n: " + str(n))
    print("Применяем алгоритм Полларда ро эвристики для факторизации n")
    div_1 = PollardRho(n)
    div_2 = n//div_1

    print("Первый делитель для n: ", div_1)
    print("Второй делитель для n: ", div_2)
    fi_find = phi(div_1, div_2)
    print("Фи = " + str(fi_find))
    print("Применяем алгоритм Евклида для нахождения закрытой экспоненты")
    d_find = Evklid_alg_extended(e, fi_find)
    if d_find < 0:  # если d меньше 0, прибавляем фи
        d_find = d_find + fi_find
    print("Найденная закрытая экспонента d: " + str(d_find))
    print("Найденный закрытый ключ (d, n): " + str(d_find) + ", " + str(n))

    time_1 = timeit.default_timer() - start_timer
    print("Время выполнения: " + str(time_1) + " сек")


######################################################################


if __name__ == '__main__':
    l = 120
    e, n, d = key_gen(l)  # находит n
    # print(e, n, d)
    enc = RSA_encryption(l, e, n)
    dec = RSA_decryption(enc, d, n, l)

    # Атака!!!
    RSA_attack(e, n)



