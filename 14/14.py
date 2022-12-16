occupied = set()
floor = 0

for line in open('14.txt'):
  xy = [list(map(int, c.split(','))) for c in line.strip().split(' -> ')]
  for i in range(len(xy) - 1):
    (x1, y1), (x2, y2) = xy[i], xy[i+1]
    (x1, x2), (y1, y2) = sorted([x1, x2]), sorted([y1, y2])
    for x in range(x1, x2+1):
      for y in range(y1, y2+1):
        occupied.add(x + y * 1j)
        floor = max(floor, y + 2)

t = 0

while True:
  s = 500 + 0j
  while True:
    if (ds := s + 1j) not in occupied and ds.imag < floor:
      s += 1j
      continue
    if (ds := s + 1j - 1) not in occupied and ds.imag < floor:
      s += 1j - 1
      continue
    if (ds := s + 1j + 1) not in occupied and ds.imag < floor:
      s += 1j + 1
      continue
    if s in occupied:
      print(t)
      exit(0)
    occupied.add(s)
    t += 1
    break
