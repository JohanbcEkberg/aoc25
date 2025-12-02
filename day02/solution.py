def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.read().strip().split(",")

def part1():
  data = read_input("input")
  ids = []
  for item in data:
    low, high = map(int, item.split("-"))

    for num in range(low, high + 1):
      s = str(num)
      first_half = s[:len(s)//2]
      second_half = s[len(s)//2:]

      if first_half == second_half:
        ids.append(num)

  return sum(ids)

def part2():
  pass

if __name__ == "__main__":
  print("Part 1:", part1())
  print("Part 2:", part2())