def read_input(path):
  res = []
  with open(path) as f:
    lines = f.read().strip().splitlines()
    for line in lines:
      nums = list(map(int, line.split(",")))
      res.append((nums[0], nums[1]))
  return res

def part1():
  data = read_input("./input")
  max = 0
  N = len(data)
  for i in range(N):
    for j in range(i, N):
      p1 = data[i]
      p2 = data[j]
      diff_x = abs(p1[0] - p2[0]) + 1
      diff_y = abs(p1[1] - p2[1]) + 1
      prod = diff_x * diff_y
      if prod > max:
        max = prod
  return max


def part2():
  pass

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")