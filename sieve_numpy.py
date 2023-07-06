"""Implementation of the sieve of Eratosthenes utilizing NumPy arrays"""
import numpy as np


def sieve(n):
    """Implementation of the sieve of Eratosthenes utilizing NumPy arrays"""
    # prepare array of primes with first two positions as False
    primes = np.ones(n, dtype=np.bool_)
    primes[:2] = False

    # loop over primes and mark composite numbers
    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            primes[p * p: n : p] = False

    # Count the prime numbers
    prime_count = np.sum(primes)
    return prime_count

print(sieve(2**32))
