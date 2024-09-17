def is_palindrome(number):
  og_num = number
  reverse_num = 0
  while number != 0:
    reverse_num = reverse_num * 10
    reverse_num = reverse_num + (number % 10)
    number = int(number / 10)
  return og_num == reverse_num

def largest_three_digit_product_palindrone():
  largest_product = 1
  for i in range(100, 1000):
    for j in range(1000, i, -1):
      product = i * j
      if product < largest_product:
        # Optimization
        continue
      elif is_palindrome(product):
        largest_product = max(largest_product, product)
  return largest_product

print(largest_three_digit_product_palindrone())