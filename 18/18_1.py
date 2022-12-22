cubes = {tuple(map(int,l.split(','))) for l in open('18.txt')}
sides = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

seen = set()

added = []

res = 0
for x, y, z in cubes:
  res += 6
  for side in sides(x, y, z):
    if side in seen: res -= 2
  seen.add((x, y, z))

print(res)