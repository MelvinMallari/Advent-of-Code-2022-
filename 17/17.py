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

num_rocks = 0
NUM_SIMS = 2022
rock = {r.real + 2 + (r.imag + height + 3)*1j for r in rocks[0]}
a = []

while num_rocks < NUM_SIMS:
  if num_rocks % 100 == 0: print(num_rocks)
  for jet in jets:
    moved = {r + jet for r in rock}
    if all(lwall < m.real < rwall for m in moved) and not (moved & solid):
      rock = moved
    moved = {r - 1j for r in rock} 
    if (moved & solid):
      solid |= rock
      o = height
      height = max((s.imag for s in solid)) + 1
      a.append(int(height - o))
      num_rocks += 1
      if num_rocks >= NUM_SIMS: break
      rock = {r.real + 2 + (r.imag + height + 3)*1j for r in rocks[num_rocks%5]}
    else:
      rock = moved

print(a)
print(int(height))