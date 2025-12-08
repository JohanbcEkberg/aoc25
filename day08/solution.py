class DSU:
  def __init__(self, n):
    self.parent = list(range(n))
    self.size = [1] * n
    self.num_sets = n

  def find(self, i):
    if self.parent[i] == i:
      return i
    self.parent[i] = self.find(self.parent[i])
    return self.parent[i]

  def union(self, i, j):
    root_i = self.find(i)
    root_j = self.find(j)

    if root_i != root_j:
      if self.size[root_i] < self.size[root_j]:
        root_i, root_j = root_j, root_i

      self.parent[root_j] = root_i
      self.size[root_i] += self.size[root_j]
      self.num_sets -= 1
      return True
    return False

  def get_circuit_sizes(self):
    sizes = []
    for i in range(len(self.parent)):
      if self.parent[i] == i:
        sizes.append(self.size[i])
    return sizes

def read_input(filename):
  coords = []
  with open(filename, 'r') as file:
    for line in file.read().splitlines():
      line = line.strip()
      if line:
        coords.append(tuple(map(int, line.split(','))))
  return coords


def dist(p1, p2):
  return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def part1():
  coords = read_input("./input")
  connections_to_make = len(coords)
  N = len(coords)

  all_edges = []
  for i in range(N):
    for j in range(i + 1, N):
      dist_sq = dist(coords[i], coords[j])
      all_edges.append((dist_sq, i, j))

  all_edges.sort(key=lambda x: x[0])

  dsu = DSU(N)
  connections_made = 0

  for dist_sq, i, j in all_edges:
    dsu.union(i, j)
    connections_made += 1
    if connections_made == connections_to_make:
      break

  circuit_sizes = dsu.get_circuit_sizes()
  circuit_sizes.sort(reverse=True)
  
  sizes_to_multiply = circuit_sizes[:3]

  result = sizes_to_multiply[0] * sizes_to_multiply[1] * sizes_to_multiply[2]

  return result

def part2():
  coords = read_input("./input")
  N = len(coords)

  all_edges = []
  for i in range(N):
    for j in range(i + 1, N):
      dist_sq = dist(coords[i], coords[j])
      all_edges.append((dist_sq, i, j, coords[i], coords[j]))

  all_edges.sort(key=lambda x: x[0])

  dsu = DSU(N)

  last_ci = None
  last_cj = None
  for dist_sq, i, j, ci, cj in all_edges:
    dsu.union(i, j)
    if len(dsu.get_circuit_sizes()) == 1:
      last_ci = ci
      last_cj = cj
      break

  result = last_ci[0] * last_cj[0]
  return result


if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")