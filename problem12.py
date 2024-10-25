def get_devisors_for_num(devisors_map, num):
  devisors_set = set([])
  temp_num = num
  for i in range(1, num + 1):
    if temp_num == 0:
      break
    
    if num % i == 0 and devisors_map.get(i):
      devisors_set = devisors_set | devisors_map.get(i)
      temp_num = temp_num / i
  devisors_set.add(num)
  return devisors_set

def compute_devisors(number_of_devisors):
  devisors_map = {}

  for i in range(10):
    devisors = get_devisors_for_num(devisors_map, i)
    devisors_map[i] = devisors

  return devisors_map

print(compute_devisors(500))