"""GPU accelerated implementation of the sieve of Eratosthenes using CuPy"""
import cupy as cp


def sieve(n):
    """GPU accelerated implementation of the sieve of Eratosthenes using CuPy"""
    # prepare array of primes with first two positions as False
    primes = cp.ones(n, dtype=cp.bool_)
    primes[:2] = False

    # loop over primes and mark composite numbers
    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            primes[p * p: n : p] = False

    # Count the prime numbers
    prime_count = cp.sum(primes)
    return prime_count


print(sieve(2**32))
