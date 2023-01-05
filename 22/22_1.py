import re

grid = []
done = False

for line in open('22.txt'):
  line = line[:-1]

  if line == '':
    done = True
  if done:
    sequence = line
  else:
    grid.append(line)

max_width = max(map(len, grid))
grid = [line + ' ' * (max_width - len(line)) for line in grid]

row, col = 0, 0
# start off moving right
dr, dc = 0, 1

while grid[row][col] != '.':
  col += 1

for x, y in re.findall(r"(\d+)([RL]?)", sequence):
  x = int(x)
  for _ in range(x):
    next_row = row
    next_col = col
    while True:
      next_row = (next_row + dr) % len(grid)
      next_col = (next_col + dc) % len(grid[0])

      # keep moving until we wrap around
      if grid[next_row][next_col] != ' ':
        break

    # hit wall, break, don't apply move
    if grid[next_row][next_col] == '#':
      break

    # commit move
    row, col = next_row, next_col

  # turn logic
  if y == 'R':
    dr, dc = dc, -dr
  elif y == 'L':
    dr, dc = -dc, dr


if dr == 0: 
  if dc == 1: # right
    d = 0
  else: # left
    d = 2
else:
  if dr == 1: # down 
    d = 1
  else: # up
    d = 3


print(1000 * (row + 1) + 4 * (col + 1) + d)

