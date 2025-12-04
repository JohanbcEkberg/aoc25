class Grid:
  def __init__(self, lines):
    self.matrix = [list(map(self.symb_to_bool, list(line))) for line in lines]

  def number_of_neighbors(self, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
      r, c = row + dr, col + dc
      if 0 <= r < len(self.matrix) and 0 <= c < len(self.matrix[0]):
        count += self.matrix[r][c]
    return count

  def symb_to_bool(self, symb):
    if symb == "@":
      return True
    elif symb == ".":
      return False
    else:
      raise ValueError(f"Invalid symbol: {symb}")

def read_input(path):
  with open(path, "r") as f:
    return f.read().strip().splitlines()

def part1():
  data = read_input("./input")
  grid = Grid(data)
  count = 0
  for row in range(len(grid.matrix)):
    for col in range(len(grid.matrix[0])):
      if grid.matrix[row][col]:
        neighbors = grid.number_of_neighbors(row, col)
        if neighbors < 4:
          count += 1
  return count

def part2():
  data = read_input("./input")
  grid = Grid(data)
  count = 0
  found = True

  while found:
    found = False
    for row in range(len(grid.matrix)):
      for col in range(len(grid.matrix[0])):
        if grid.matrix[row][col]:
          neighbors = grid.number_of_neighbors(row, col)
          if neighbors < 4:
            grid.matrix[row][col] = False
            found = True
            count += 1

  return count

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")