rocks = [
  [0, 1, 2, 3],
  [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
  [0, 1, 2, 2 + 1j, 2 + 2j],
  [0, 1j, 2j, 3j],
  [0, 1, 1j, 1 + 1j]
]

jets = [1 if l == '>' else -1 for l in open('17.txt').read()]
solid = {x - 1j for x in range(7)}
lwall, rwall = -1, 7
height = 0
seen = {}

num_rocks = 0
TARGET_ROCKS = 1000000000000
rock = {r.real + 2 + (r.imag + height + 3)*1j for r in rocks[0]}
offset = 0

# summarize the top skyline for the last 20 rows
def summarize():
  o = [-20]*7

  for x in solid:
    r = int(x.real)
    i = int(x.imag)
    o[r] = max(o[r], i)
  
  t = max(o)
  return tuple(x - t for x in o)

while num_rocks < TARGET_ROCKS:
  for j, jet in enumerate(jets):
    moved = {r + jet for r in rock}
    if all(lwall < m.real < rwall for m in moved) and not (moved & solid):
      rock = moved
    moved = {r - 1j for r in rock} 
    if (moved & solid):
      solid |= rock
      height = int(max((s.imag for s in solid)) + 1)
      num_rocks += 1
      rock_index = num_rocks%5
      key = (rock_index, j, summarize())
      if key in seen:
        cycle_start_rocks, cycle_start_height = seen[key]
        cycle_rocks = num_rocks - cycle_start_rocks
        cycle_height = height - cycle_start_height
        rocks_remaining = TARGET_ROCKS - num_rocks
        num_cycles = rocks_remaining // cycle_rocks
        offset = num_cycles * cycle_height
        num_rocks += num_cycles * cycle_rocks
        seen = {}
      seen[key] = (num_rocks, height)
      if num_rocks >= TARGET_ROCKS: break
      rock = {r.real + 2 + (r.imag + height + 3)*1j for r in rocks[rock_index]}
    else:
      rock = moved

print(height + offset)