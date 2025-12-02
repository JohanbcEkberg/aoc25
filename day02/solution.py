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

def split_chunks(s, n):
  chunk_set = set()
  for i in range(0, len(s), n):
    chunk_set.add(s[i:i+n])
  return chunk_set

def is_valid_id_part_2(num):
  s = str(num)
  for i in range(1, len(s)):
    if len(s) % i == 0:
      chunks = split_chunks(s, i)
      if len(chunks) == 1:
        return True
  return False


def part2():
  data = read_input("input")
  ids = []
  for item in data:
    low, high = map(int, item.split("-"))

    for num in range(low, high + 1):
      if is_valid_id_part_2(num):
        ids.append(num)

  return sum(ids)

if __name__ == "__main__":
  print("Part 1:", part1())
  print("Part 2:", part2())