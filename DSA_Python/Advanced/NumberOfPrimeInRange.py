"""
Given a range of integers, count the number of prime numbers in that range.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for n in range(start, end + 1):
        if is_prime(n):
            count += 1
    return count
# Example usage:
start = 1
end = 5
print(count_primes_in_range(start, end))  # Output: 4 (11, 13, 17, 19 are prime)
