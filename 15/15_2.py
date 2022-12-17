import re

pattern = re.compile(r"-?\d+")

lines = [list(map(int, pattern.findall(l))) for l in open('15.txt')]

N = 4000000

for Y in range(N+1):
  intervals = []
  for sx, sy, bx, by in lines:

    dist = abs(sx - bx) + abs(sy - by)

    z = dist - abs(sy - Y)

    # out sensor's range
    if z < 0: continue

    intervals.append([sx - z, sx + z])

  merged = []
  intervals.sort(key=lambda x: x[0])
  curr = intervals[0]

  for s, e in intervals[1:]:
    if s <= curr[1]:
      curr[1] = max(curr[1], e)
    else:
      merged.append(curr)
      curr = [s, e]

  merged.append(curr)

  x = 0
  for lo, hi in merged:
    if x < lo:
      print(x*4000000 + Y)
      exit(0)
    x = max(x, hi + 1)
    if x > N: break
