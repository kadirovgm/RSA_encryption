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

# def Evklid_alg_extended(m, n):
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
#         u2 = u1 - q * u2
#         u1 = r
#         r = v2
#         v2 = v1 - q * v2
#         v1 = r
#     d = a
#     s = u1
#     t = v1
#     print("d: " + str(d))
#     print("s: " + str(s))
#     print("t: " + str(t))
#     return s
#
# print(Evklid_alg_extended(11,143))
import random
import math


# Function to calculate (base^exponent)%modulus
def modular_pow(base, exponent, modulus):
    # initialize result
    result = 1

    while (exponent > 0):

        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1

        # base = base * base
        base = (base * base) % modulus

    return result


# method to return prime divisor for n
def PollardRho(n):
    # no prime divisor for 1
    if (n == 1):
        return n

    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2

    # we will pick from the range [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x

    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = (random.randint(0, 1) % (n - 1))

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):

        # Tortoise Move: x(i+1) = f(x(i))
        x = (modular_pow(x, 2, n) + c + n) % n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)

    return d


# Driver function
if __name__ == "__main__":
    n = 12
    print("One of the divisors for", n, "is ", PollardRho(n))

# This code is contributed by chitranayal