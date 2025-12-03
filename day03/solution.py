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

def get_biggest_number(s: str) -> tuple[int, str]:
  res = (0, '0')

  for i in range(len(s)):
    idx, num = res
    if s[i] > num:
      num = s[i]
      idx = i
    res = (idx, num)
  
  return res

def part2() -> int:
  data = read_input("./input")
  jolts = []

  for line in data:
    line_len = len(line)
    s = []
    curr_index = 0
    for i in range(12, 0, -1):
      check = line[curr_index:line_len-i+1]
      checked = get_biggest_number(check)
      curr_index += checked[0] + 1
      s.append(checked[1])

    jolts.append(''.join(s))

  return sum(map(int, jolts))

if __name__ == "__main__":
  print("Part 1:", part1())
  print("Part 2:", part2())