def read_input(path):
  res = []
  with open(path) as f:
    for line in f.read().strip().splitlines():
      parts = line.split(" ")
      indicator = None
      buttons = []
      jolts = None
      for part in parts:
        if part[0] == '[':
          wanted = list(part[1:-1])
          wanted = list(map(lambda x: True if x == '#' else False, wanted))
          indicator = wanted
        elif part[0] == '(':
          button = part[1:-1]
          indicies = list(map(int, button.split(",")))
          buttons.append(indicies)
        elif part[0] == '{':
          joltages = part[1:-1].split(",")
          jolts = list(map(int, joltages))
      res.append((indicator, buttons, jolts))
  return res


def solve_row1(indicator, buttons):
  n = len(indicator)
  m = len(buttons)
  A = [[0] * m for _ in range(n)]
  for j, btn in enumerate(buttons):
    for i in btn:
      A[i][j] = 1
  b = [1 if x else 0 for x in indicator]
  M = [A[i][:] + [b[i]] for i in range(n)]
  pivot_col = [-1] * n
  row = 0
  col = 0
  while row < n and col < m:
    pivot_row = None
    for r in range(row, n):
      if M[r][col] == 1:
        pivot_row = r
        break
    if pivot_row is None:
      col += 1
      continue
    if pivot_row != row:
      M[row], M[pivot_row] = M[pivot_row], M[row]
    pivot_col[row] = col
    for r in range(n):
      if r != row and M[r][col] == 1:
        for c in range(col, m+1):
          M[r][c] ^= M[row][c]
    row += 1
    col += 1
  rank = row
  x0 = [0] * m
  for r in range(rank):
    c = pivot_col[r]
    s = M[r][m]
    for cc in range(c+1, m):
      if M[r][cc] and x0[cc]:
        s ^= 1
    x0[c] = s
  pivot_set = set(pivot_col[:rank])
  free_cols = [c for c in range(m) if c not in pivot_set]
  nullspace = []
  for free in free_cols:
    vec = [0]*m
    vec[free] = 1
    for r in range(rank):
      c = pivot_col[r]
      s = 0
      for j in range(c+1, m):
        if M[r][j] and vec[j]:
          s ^= 1
      vec[c] = s
    nullspace.append(vec)
  k = len(nullspace)
  if k <= 20:
    best = None
    best_sum = 10**9
    for mask in range(1 << k):
      x = x0[:]
      mm = mask
      idx = 0
      while mm:
        if mm & 1:
          v = nullspace[idx]
          for i in range(m):
            x[i] ^= v[i]
        mm >>= 1
        idx += 1
      w = sum(x)
      if w < best_sum:
        best_sum = w
        best = x
    return best_sum
  best = x0[:]
  best_sum = sum(best)
  improved = True
  while improved:
    improved = False
    for v in nullspace:
      cand = [(a ^ b) for a, b in zip(best, v)]
      s = sum(cand)
      if s < best_sum:
        best = cand
        best_sum = s
        improved = True
  return best_sum


def part1():
  machines = read_input("./input")
  total = 0
  for (indicator, buttons, _) in machines:
      total += solve_row1(indicator, buttons)
  return total


def part2():
  pass


if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")
