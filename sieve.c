#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>

__uint64_t sieve(__uint64_t n) {
    // Allocate memory for primes array on the heap
    bool* primes = (bool*)malloc((n) * sizeof(bool));
    if (primes == NULL) {
        printf("Failed to allocate memory.\n");
        return -1;
    }

    // Initialize primes array
    for (__uint64_t i = 0; i < n; i++) {
        if (i < 2)
            primes[i] = false;
        else
            primes[i] = true;
    }

    // Loop over primes and mark composite numbers
    for (__uint64_t p = 2; p <= sqrt(n); p++) {
        if (primes[p]) {
            for (__uint64_t i = p * p; i < n; i += p) {
                primes[i] = false;
            }
        }
    }

    // Count the prime numbers
    __uint64_t prime_count = 0;
    for (__uint64_t i = 0; i < n; i++) {
        if (primes[i])
            prime_count++;
    }

    // Free the allocated memory
    free(primes);

    return prime_count;
}

int main() {
    printf("%d\n", sieve(4294967296));  // 4294967296 = 2**32
    return 0;
}
