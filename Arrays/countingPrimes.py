def count_primes(n):
    # If n is less than or equal to 2, there are no primes less than n
    if n <= 2:
        return 0

    # Step 1: Initialize a list to track prime status of each number from 0 to n-1
    is_prime = [True] * n

    # Step 2: 0 and 1 are not prime numbers
    is_prime[0] = is_prime[1] = False

    # Step 3: Use the Sieve of Eratosthenes algorithm
    # Loop from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If i is prime
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, n, i):
                is_prime[j] = False

    # Step 4: Count how many numbers are still marked as prime
    return sum(is_prime)

# Example usage:
print(count_primes(10))  # Output: 4
print(count_primes(0))   # Output: 0
print(count_primes(1))   # Output: 0
