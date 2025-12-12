def read_input(path):
  shapes = None
  regions = None
  with open(path) as f:
    parts = f.read().strip().split("\n\n")
    shapes = parts[:-1]
    regions = parts[-1].split("\n")

  pshapes = {}
  for s in shapes:
    (name, shape) = s.split(":")
    pshapes[name] = shape
  
  pregions = []
  for r in regions:
    (dim, nums) = r.split(": ")
    (R, C) = map(int, dim.split("x"))
    pregions.append(((R, C), list(map(int, nums.split(" ")))))
    
  return (pshapes, pregions)
  
def solve_region(shapes, region):
  shape_sizes = {}
  for shape in shapes:
    size = 0
    for c in shapes[shape]:
      if c == "#":
        size += 1
    shape_sizes[shape] = size
  
  R, C = region[0]
  region_size = R * C
  shapes_size = 0
  for name, count in enumerate(region[1]):
    shapes_size += (count * shape_sizes.get(str(name), 0))

  return region_size > shapes_size # Based on guesstimate

def part1():
  (shapes, regions) = read_input("./input")
  total = 0
  for region in regions:
    total += solve_region(shapes, region) 
  return total

if __name__ == "__main__":
  print(f"Part 1: {part1()}")