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
    return rec(matrix, row, col + 1) + rec(matrix, row, col - 1) + 1
  else:
    raise ValueError("Value of matrix[row][col] is " + matrix[row][col])

def part1():
  matrix = read_input("./input")
  idx = 0
  while matrix[0][idx] != 'S':
    idx += 1

  return rec(matrix, 1, idx)

def rec2(matrix: list[list[str]], row: int, col: int, memo: dict) -> int:
  while row < len(matrix) and matrix[row][col] == '.':
    matrix[row][col] = '|'
    row += 1

  mem_key = (row, col)

  if mem_key in memo:
    return memo[mem_key]

  res = 0
  if row == len(matrix):
    res = 1
  elif matrix[row][col] == '|':
    res = rec2(matrix, row + 1, col, memo)
  elif matrix[row][col] == '^':
    res = rec2(matrix, row, col + 1, memo) + rec2(matrix, row, col - 1, memo)
  else:
    raise ValueError("Value of matrix[row][col] is " + matrix[row][col])

  memo[mem_key] = res
  return res
  
def part2():
  matrix = read_input("./input")
  idx = 0
  while matrix[0][idx] != 'S':
    idx += 1

  memo = {}
  res = rec2(matrix, 1, idx, memo)

  return res

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")