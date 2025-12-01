def read_input(path) -> str:
  with open(path, "r") as file:
    return file.read().strip().splitlines()

def part1():
  ptr = 50
  res = 0
  for line in read_input("./input"):
    pair = (line[0], line[1:])
    sign = 1 if pair[0] == 'R' else -1
    num = int(pair[1])
    rot = num * sign

    ptr = (ptr + rot) % 100
    if ptr == 0:
      res += 1 
  return res

    

if __name__ == "__main__":
  print("Part 1:", part1())