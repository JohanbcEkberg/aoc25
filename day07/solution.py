def read_input(path):
  with open(path) as f:
    lines = f.read().strip().splitlines()
    return [list(line) for line in lines]
  

def rec(matrix: list[list[str]], row: int, col: int) -> int:
  while row < len(matrix) and matrix[row][col] == '.':
    matrix[row][col] = '|'
    row += 1
  
  if row == len(matrix):
    return 0
  elif matrix[row][col] == '|':
    return 0
  elif matrix[row][col] == '^':
    return rec(matrix, row + 1, col + 1) + rec(matrix, row + 1, col - 1) + 1
  else:
    raise ValueError("Value of matrix[row][col] is ", matrix[row][col])

def part1():
  matrix = read_input("./input")
  idx = 0
  while matrix[0][idx] != 'S':
    idx += 1

  return rec(matrix, 1, idx)

def part2():
  pass

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")