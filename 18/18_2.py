cubes = {tuple(map(int,l.split(','))) for l in open('18.txt')}
sides = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

# determine grid boundaries
min_c, max_c = float('inf'), float('-inf')
for x, y, z in cubes:
  min_c = min(min_c, x, y, z)
  max_c = max(max_c, x, y, z)
min_c -= 1
max_c += 1

seen = set()
todo = [(min_c, min_c, min_c)]
# flood fill, keep track of faces seen
while todo:
  here = todo.pop()
  for s in (sides(*here) - cubes - seen):
    if all(min_c <= c <= max_c for c in s):
      todo.append(s)
  seen |= {here}

# for the cubes, sum all faces seen by the flood fill
res = 0 
for c in cubes:
  for s in sides(*c):
    if s in seen: res += 1

print(res)