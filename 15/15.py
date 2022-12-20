import re

# pt1 notes, math
# solve for range of x
# dist = abs(sx - bx) + abs(sy - by)
# abs(x - sx) + abs(y - sy) <= dist
# abs(x - sx) <= dist - abs(y - sy)
# we we want to know for row Y specifically, fill that in for y
# abs(x - sx) <= dist - abs(Y - sy)
# let z = dist - abs(Y - sy)
# x - sx <= [-z, +z]
# x <= [sx - z, sx + z]
# range of values:
# sx - z <= x <= sx + z

pattern = re.compile(r"-?\d+")
Y = 2000000
intervals = []
known = set()

for line in open('15.txt'):
  sx, sy, bx, by = map(int, pattern.findall(line))

  dist = abs(sx - bx) + abs(sy - by)
  z = dist - abs(sy - Y)

  # out sensor's range
  if z < 0: continue

  intervals.append([sx - z, sx + z])

  if by == Y: known.add(bx)


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

res = 0
for lo, hi in merged:
  res += hi - lo + 1
  for k in known:
    if lo <= k <= hi: res -= 1

print(res)