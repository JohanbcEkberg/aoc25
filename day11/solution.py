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

def part2():
  pass

if __name__ == "__main__":
  print("Part 1:", part1())
  print("Part 2:", part2())