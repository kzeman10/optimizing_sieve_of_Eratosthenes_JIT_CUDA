"""This pure Python naive implementation of sieve of Erathostenes uses list of booleans and two nested loops to solve the selected problem"""


def sieve(n):
    """naive Python impleentation for sieve of Erathostenes"""
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
