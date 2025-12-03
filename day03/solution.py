def read_input(path):
  with open(path, 'r') as file:
    return file.read().strip().splitlines()

def part1() -> int:
  data = read_input("./input")
  jolts = []
  for line in data:
    first = '0'
    second = '0'
    idx_of_first = 0

    for i in range(len(line) - 1):
      if line[i] > first:
        idx_of_first = i
        first = line[i]

    for i in range(idx_of_first + 1, len(line)):
      if line[i] > second:
        second = line[i]
    
    num = f'{first}{second}'
    jolts.append(int(num))
  
  return sum(jolts)

def part2():
  pass

if __name__ == "__main__":
  print("Part 1:", part1())
  print("Part 2:", part2())