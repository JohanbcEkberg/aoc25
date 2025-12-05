def read_input(path) -> tuple[list[tuple[int, int]], list[int]]:
  ranges = []
  ids = []
  with open(path, "r") as f:
    for line in f.read().strip().splitlines():
      if "-" in line:
        low, high = line.split("-")
        ranges.append((int(low), int(high)))
      elif "" != line:
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
  ranges, _ = read_input("./input")
  merged_ranges: list[tuple[int, int]] = []
  for r in sorted(ranges):
    current_highest = r if len(merged_ranges) == 0 else merged_ranges[-1]
    if current_highest[1] < r[0] - 1:
      merged_ranges.append(r)
    else:
      new_high_limit = max(current_highest[1], r[1])
      new_high_range = (current_highest[0], new_high_limit)
      if len(merged_ranges) == 0:
        merged_ranges.append(new_high_range)
      else:
        merged_ranges[-1] = new_high_range
  
  return sum(high - low + 1 for (low, high) in merged_ranges)

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")