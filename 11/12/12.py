from collections import deque

data = open('12.txt', 'r').read()
grid = [list(l) for l in data.split('\n')]
m, n = len(grid), len(grid[0])
for i in range(m):
  for j in range(n):
    if grid[i][j] == 'S': grid[i][j] = 'a'
    if grid[i][j] == 'E': 
      start_x, start_y = i, j
      grid[i][j] = 'z'
  
# bfs from end to start to share algorithm b/w pt1 & pt2
def bfs(c, d):
  dist = {(c, d): 0}
  q = deque([(c, d)])
  while len(q) > 0:
    i, j = q.popleft()
    if grid[i][j] == 'a': return dist[(i, j)]
    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
      if (0 <= x < m and 0 <= y < n and (x, y) not in dist and ord(grid[i][j]) - ord(grid[x][y]) <= 1):
        dist[(x, y)] = dist[(i, j)] + 1
        q.append((x, y))

print(bfs(start_x, start_y))
