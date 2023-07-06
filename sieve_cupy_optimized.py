"""GPU optimized implementation of the sieve of Eratosthenes using CUPY and NumPy"""
import numpy as np
import cupy as cp


def sieve_np(n):
    """Implementation of the sieve of Eratosthenes utilizing NumPy arrays"""
    # prepare array of primes with first two positions as False
    primes = np.ones(n, dtype=np.bool_)
    primes[:2] = False

    # loop over primes and mark composite numbers
    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            primes[p * p: n : p] = False

    # extract prime numbers indices
    primes = np.flatnonzero(primes)
    return primes


def sieve_cp(n):
    """Optimized implementation of the sieve of Eratosthenes using CuPy"""
    # prepare array of primes with first two positions as False
    primes = cp.ones(n, dtype=cp.bool_)
    primes[:2] = False
    primes_small = sieve_np(int(n ** 0.5) + 1)

    # loop over primes and mark composite numbers
    for p in primes_small:
        primes[p * p: n : p] = False

    # Count the prime numbers
    prime_count = cp.sum(primes)
    return prime_count


print(sieve_cp(2**32))
