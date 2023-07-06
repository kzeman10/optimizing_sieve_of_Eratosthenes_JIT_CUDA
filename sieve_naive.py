"""Naive pure-Python implementation of the sieve of Erathostenes using a list"""


def sieve(n):
    """Naive pure-Python implementation of the sieve of Erathostenes using a list"""
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

print(sieve(2**30))
