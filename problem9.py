
def get_first_pythagorean_triplet_product(expected_sum):
  for i in range(1, expected_sum - 2):
    for j in range(i + 1, expected_sum - 1):
      sum_i_and_j = i + j
      if sum_i_and_j > expected_sum:
        break
      for k in range(j + 1, expected_sum):
        sum = sum_i_and_j + k
        if sum > expected_sum:
          break
        if sum < expected_sum:
          continue   
        # a^2 + b^c = c^2
        if i**2 + j**2 == k**2:
          return i*j*k
  # Should hopefully never reach
  return -1

print(get_first_pythagorean_triplet_product(1000))