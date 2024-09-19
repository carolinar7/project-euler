import sys

# Basing this solution off of the Fundamental Theorem of Arithmetic.
# The theorem describes that every postive number that is not 1
# is either a prime number or can be constructed by solely prime numbers.
# Storing the prime numbers calculated to facilitate classification of
# new numbers as prime numbers.

def is_prime_number(prime_list, num):
  for prime in prime_list:
    if num % prime == 0:
      return False
  return True

def add_next_prime_num_to_prime_list(prime_list):
  last_prime = prime_list[-1]
  for i in range(last_prime + 1, sys.maxsize):
    if is_prime_number(prime_list, i):
      prime_list.append(i)
      return

def get_nth_prime_number(n):
  prime_list = [2]
  while len(prime_list) != n:
    add_next_prime_num_to_prime_list(prime_list)
  return prime_list[-1]

print(get_nth_prime_number(10001))