import sys
import math

# Basing this solution off of the Fundamental Theorem of Arithmetic.
# The theorem describes that every postive number that is not 1
# is either a prime number or can be constructed by solely prime numbers.
# Storing the prime numbers calculated to facilitate classification of
# new numbers as prime numbers.

def is_prime_number(prime_list, num):
  # This line right here did the trick! It went from very slow :( to
  # very very fast ;) The idea here, thank you reddit, is that 
  # if there is a factor that is above the square root of the number
  # then there must be a factor below the square root. Therefore,
  # we can safely check up to the square root of num against saved
  # prime numbers.
  sqrt_of_num = math.sqrt(num)

  for prime in prime_list:
    if num % prime == 0:
      return False

    if prime >= sqrt_of_num:
      break

  return True

def add_next_prime_num_to_prime_list(prime_list):
  last_prime = prime_list[-1]
  for i in range(last_prime + 1, sys.maxsize):
    if is_prime_number(prime_list, i):
      prime_list.append(i)
      return

def get_prime_numbers_up_to_n(n):
  prime_list = [2]
  while prime_list[-1] < n:
    add_next_prime_num_to_prime_list(prime_list)
  # The last prime is over n. Let's remove it.
  prime_list.pop()
  return prime_list

def summation_primes_up_to_n(n):
  prime_numbers = get_prime_numbers_up_to_n(n)
  sum = 0
  for number in prime_numbers:
    sum += number
  return sum

print(summation_primes_up_to_n(2000000))