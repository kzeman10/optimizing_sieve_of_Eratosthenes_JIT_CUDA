"""JIT-compiled implementation of the sieve of Eratosthenes by Numba"""
import numba as nb


@nb.njit()
def sieve(n):
    """JIT-compiled implementation of the sieve of Eratosthenes by Numba"""
    # prepare list of primes with first two positions as False
    primes = [False if i < 2 else True for i in range(n)]

    # loop over primes and mark composite numbers
    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False

    # Count the prime numbers
    prime_count = sum(primes)
    return prime_count

print(sieve(2**32))
