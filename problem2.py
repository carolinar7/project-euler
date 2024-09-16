def sum_of_even_fibonocci_values(upper_bound):
  sum = 0
  fib = [0, 1, 1]
  while (fib[2] < upper_bound):
    result = fib[2] + fib[1]
    fib[0] = fib[1]
    fib[1] = fib[2]
    fib[2] = result
    if (result % 2 == 0):
      sum += result
  return sum

print(sum_of_even_fibonocci_values(4000000))

