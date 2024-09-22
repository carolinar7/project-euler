# This algorithm works by shifting a window of size n across the 1000
# numbers. We memoize our computed product to compute the next product.
# Unless, we encounter a 0 which will result in a reset of our product
# count.

# If we encounter a 0 we run this method that resets our digits, the 
# remaining given number, and the product of the returned digits.
def shift_reset(n, given_num):
  digits = []
  # Shift over once, skipping the 0.
  given_num = given_num // 10

  new_product = 1
  for _ in range(n):
    if given_num == 0:
      break
    next_digit = given_num % 10
    # Let's shift/reset again if we find a 0.
    if next_digit == 0:
      return shift_reset(n, given_num)
    given_num = given_num // 10
    new_product *= next_digit
    digits.append(next_digit)

  return [digits, given_num, new_product]

# Let's make the assumption that:
# 1 < n <= len(digit) 
def max_adjacent_n_digits_product(n, given_num):
  digits = []

  # Lets do an initial computation of the first n digits.
  # We will memoize based on this initial computation.
  max = 1
  for _ in range(n):
    next_digit = given_num % 10
    if next_digit == 0:
      digits, given_num, max = shift_reset(n, given_num)
      break
    digits.append(given_num % 10)
    max = max * next_digit
    given_num = given_num // 10
  
  last_product = max
  while given_num != 0:
    next_digit = given_num % 10

    if next_digit == 0:
      digits, given_num, last_product = shift_reset(n, given_num)
    else:
      # Since we are sliding a window, we know that
      # we can continue to use the product we previously
      # computed. We just shift and recompute the value
      # given the next digit to add within our digits list. 
      saved_product = last_product / digits[0]
      digits.pop(0)
      digits.append(next_digit)
      given_num = given_num // 10
      last_product = saved_product * next_digit 

    if last_product > max:
      max = last_product
  
  return max

import time
start = time.perf_counter()
max_adjacent_n_digits_product(13, 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
end = time.perf_counter()
print("Elapsed time:", end-start)