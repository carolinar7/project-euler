"""
LCM can be defined as so:
      | a * b | 
      -----------
      gcd(a, b)

For each pair from 1..20, compute the LCM.
Reuse previously computed LCM within a new
LCM computation. It must chain.

The GCD algorithm used is the Euclidean
algorithm. It is very efficient.
"""

def greatest_common_divisor(num_a, num_b):
  max_num = max(num_a, num_b)
  min_num = min(num_a, num_b)

  while max_num != 0:
    remainder = max_num % min_num
    max_num = min_num
    min_num = remainder
    if remainder == 0:
      return max_num

  return 1

def least_common_multiple(num_a, num_b):
  absolute_product_of_range = abs(num_a * num_b)
  return absolute_product_of_range / greatest_common_divisor(num_a, num_b)

def smallest_multiple_for_range(range_tuple):
  start, end = range_tuple
  lcm = 1
  for i in range(start, end + 1):
    lcm = least_common_multiple(lcm, i)
  return lcm

print(smallest_multiple_for_range((1, 20)))