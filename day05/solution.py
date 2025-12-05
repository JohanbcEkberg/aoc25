def read_input(path) -> tuple[list[tuple[int, int]], list[int]]:
  ranges = []
  ids = []
  with open(path, "r") as f:
    for line in f.read().strip().splitlines():
      if "-" in line:
        low, high = line.split("-")
        ranges.append((int(low), int(high)))
      elif "" is not line:
        ids.append(int(line))


  return (ranges, ids)

def part1():
  ranges, ids = read_input("./input")
  count = 0
  for id in ids:
    for r in ranges:
      (low, high) = r
      if low <= id <= high:
        count += 1
        break

  return count

def part2():
  return 0

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")