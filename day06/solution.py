def read_input(path):
  cols = None
  with open(path, "r") as f:
    for line in f.read().strip().splitlines():
      splitted = line.split()
      if cols is None:
        cols = [[] for _ in range(len(splitted))]
      
      for i in range(len(splitted)):
        x = splitted[i]
        if x == '*' or x == '+':
          cols[i].append(x)
        else:
          cols[i].append(int(x))

  return cols

def read_input2(path):
  cols = None
  with open(path, "r") as f:
    lines = f.read().splitlines()
    cols = [[] for _ in range(len(lines[0].split()))]
    col_idx = 0
    idx = 0
    op_line = lines[-1]
    while idx < len(lines[0]):
      while op_line[idx] not in "*+":
        idx += 1
      op = op_line[idx]

      only_spaces = False
      while not only_spaces and idx < len(lines[0]):
        only_spaces = True
        num = []
        for line in lines[:-1]:
          if line[idx] in "1234567890":
            num.append(line[idx])
            only_spaces = False
        idx += 1
        if len(num) > 0:
          cols[col_idx].append(int(''.join(num)))

      cols[col_idx].append(op)
      col_idx += 1
      
  return cols


def product(xs):
  num = 1
  for i in xs:
    num *= int(i)
  return num

def part1():
  data = read_input("./input")
  res = 0

  for col in data:
    if col[-1] == '*':
      res += product(col[:-1])
    else:
      res += sum(col[:-1])

  return res

def part2():
  data = read_input2("./input")

  res = 0
  for col in data:
    if col[-1] == '*':
      res += product(col[:-1])
    else:
      res += sum(col[:-1])
  
  return res

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")