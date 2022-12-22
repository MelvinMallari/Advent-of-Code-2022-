cubes = {tuple(map(int,l.split(','))) for l in open('18.txt')}
sides = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

seen = set()
todo = [(-1,-1,-1)]

# determine grid boundaries
max_x = max_y = max_z = float('-inf')
min_x = min_y = min_z = float('inf')
for x, y, z in cubes:
  min_x, min_y, min_z = min(min_x, x), min(min_y, y), min(min_z, z)
  max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)
min_boundary = min(min_x, min_y, min_z) - 1
max_boundary = max(max_x, max_y, max_z) + 1

min_boundary = float('inf')
max_boundary = float('-inf')
for x, y, z in cubes:
  min_boundary = min(min_boundary, x, y, z)
  max_boundary = max(max_boundary, x, y, z)
min_boundary -= 1
max_boundary += 1

# flood fill, keep track of faces seen
while todo:
  here = todo.pop()
  for s in (sides(*here) - cubes - seen):
    if all(min_boundary <= c <= max_boundary for c in s):
      todo.append(s)
  seen |= {here}

# for the cubes, sum all seen faces from the flood fill
res = 0 
for c in cubes:
  for s in sides(*c):
    if s in seen:
      res += 1

print(res)