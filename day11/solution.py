def read_input(path):
  ret = {}
  with open(path, 'r') as file:
    lines = file.read().strip().splitlines()
    for line in lines:
      key, values = line.split(': ')
      values = values.split(' ')
      ret[key] = values
  return ret

def all_paths_from_you_to_out(graph, current='you', seen=set()):
  if current == 'out':
    return 1
  seen.add(current)
  total_paths = 0
  for neighbor in graph.get(current, []):
    if neighbor not in seen:
      total_paths += all_paths_from_you_to_out(graph, neighbor, seen)
  seen.remove(current)
  return total_paths

def part1():
  data = read_input("./input")
  return all_paths_from_you_to_out(data)    

def all_paths_with_fft_and_dac(graph, node, seen_fft=False, seen_dac=False, memo={}):
  key = (node, seen_fft, seen_dac)
  if node == "out":
    memo[key] = 1 if (seen_fft and seen_dac) else 0
    return memo[key]

  if node == "fft":
    seen_fft = True
  if node == "dac":
    seen_dac = True

  if key in memo:
    return memo[key]

  total = 0
  for nxt in graph.get(node, []):
    total += all_paths_with_fft_and_dac(graph, nxt, seen_fft, seen_dac, memo)

  memo[key] = total
  return total

def part2():
  data = read_input("./input")
  return all_paths_with_fft_and_dac(data, "svr")

if __name__ == "__main__":
  print("Part 1:", part1())
  print("Part 2:", part2())