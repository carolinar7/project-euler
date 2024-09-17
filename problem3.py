# Basing this solution off of the Fundamental Theorem of Arithmetic.
# The theorem describes that every postive number that is not 1
# is either a prime number or can be constructed by solely prime numbers.

import time

def is_prime(prime_list, val_to_check):
  for num in prime_list:
    if val_to_check % num == 0:
      return False
  return True

def add_next_prime_number_to_list(prime_list, range_start, range_end):
  for i in range(int(range_start), int(range_end)):
    if is_prime(prime_list, i):
      prime_list.append(i)
      return

def get_largest_prime_factor(number):
  if number <= 1:
    raise ValueError("Input a value greater than 1")
  
  prime_list = [2] # Starting off with 2 prime number

  # This must return
  while True: 
    # Interesting to see how the number and the latest prime value change
    # print(number, prime_list[-1])
    # time.sleep(.5)

    if number == prime_list[-1]:
      return number
    
    for prime in prime_list:
      if number % prime == 0:
        number = number / prime
      elif number / prime < 2:
        # Optimization: We've found the prime number.
        return number 
    
    add_next_prime_number_to_list(prime_list, prime_list[-1] + 1, number + 1)

time_start = time.perf_counter()
value = get_largest_prime_factor(600851475143)
time_end = time.perf_counter()
print(f"Result: {int(value)}. Ran in {(time_end - time_start) * 1000} milliseconds.")