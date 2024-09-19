def sum_of_squares(range_tuple):
  start, end = range_tuple
  sum = 0
  for i in range(start, end + 1):
    sum += (i**2)
  return sum

def square_of_sum(range_tuple):
  start, end = range_tuple
  sum = 0
  for i in range(start, end + 1):
    sum += i
  return sum ** 2

def sum_square_difference(range_tuple):
  return square_of_sum(range_tuple) - sum_of_squares(range_tuple)

print(sum_square_difference((1, 100)))