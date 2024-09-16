def sum_of_multiples_under_value(multiple1, multiple2, value):
  sum = 0
  for num in range(value):
    if (num % multiple1 == 0 or num % multiple2 == 0):
      sum += num
  return sum

print(sum_of_multiples_under_value(3, 5, 1000))