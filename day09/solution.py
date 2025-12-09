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
    for j in range(i + 1, N):
      p1 = data[i]
      p2 = data[j]
      diff_x = abs(p1[0] - p2[0]) + 1
      diff_y = abs(p1[1] - p2[1]) + 1
      prod = diff_x * diff_y
      if prod > max:
        max = prod
  return max

def point_in_poly(x, y, poly):
  inside = False
  n = len(poly)

  for i in range(n):
    x1, y1 = poly[i]
    x2, y2 = poly[(i + 1) % n]

    if (min(x1, x2) <= x <= max(x1, x2) and
      min(y1, y2) <= y <= max(y1, y2)):
      if (x1 == x2 == x) or (y1 == y2 == y):
        return True

    if ((y1 > y) != (y2 > y)):
      xinters = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
      if xinters >= x:
        inside = not inside

  return inside

def segment_it_outside(x1, y1, x2, y2, left, right, top, bottom):
  if x1 == x2:
    x_e = x1
    if not (left < x_e < right):
      return False
    ylo = min(y1, y2)
    yhi = max(y1, y2)
    return (yhi > top) and (ylo < bottom)
  elif y1 == y2:
    y_e = y1
    if not (top < y_e < bottom):
      return False
    xlo = min(x1, x2)
    xhi = max(x1, x2)
    return (xhi > left) and (xlo < right)
  else:
    return False


def part2():
  data = read_input("./input")
  N = len(data)

  xs = [p[0] for p in data]
  ys = [p[1] for p in data]
  min_x, max_x = min(xs), max(xs)
  min_y, max_y = min(ys), max(ys)

  best = 0

  edges = []
  for i in range(N):
    x1, y1 = data[i]
    x2, y2 = data[(i + 1) % N]
    edges.append((x1, y1, x2, y2))

  for i in range(N):
    x1, y1 = data[i]
    for j in range(i + 1, N):
      x2, y2 = data[j]

      left = min(x1, x2)
      right = max(x1, x2)
      top = min(y1, y2)
      bottom = max(y1, y2)
      area = (right - left + 1) * (bottom - top + 1)

      if area <= best:
        continue

      if left < min_x or right > max_x or top < min_y or bottom > max_y:
        continue

      corners = [
        (left, top),
        (left, bottom),
        (right, top),
        (right, bottom),
      ]
      ok = True
      for (cx, cy) in corners:
        if not point_in_poly(cx, cy, data):
          ok = False
          break
      if not ok:
        continue

      invalid = False
      for (e_x1, e_y1, e_x2, e_y2) in edges:
        if segment_it_outside(e_x1, e_y1, e_x2, e_y2, left, right, top, bottom):
          invalid = True
          break
      if invalid:
        continue

      
      if area > best:
        best = area

  return best

if __name__ == "__main__":
  print(f"Part 1: {part1()}")
  print(f"Part 2: {part2()}")