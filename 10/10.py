from collections import deque
remaining = deque([l.strip() for l in open('10.txt')])
scheduled = deque()
x = []

while len(scheduled) > 0 or len(remaining) > 0:
  next_x = x[-1] if len(x) > 0 else 1
  if (len(scheduled) > 0):
    scheduled[0][0] -= 1
    if (scheduled[0][0] == 0): 
      next_x += scheduled.popleft()[1]

  while len(scheduled) > 0 and scheduled[0][0] == 0:
    scheduled.popleft()

  if (len(remaining) > 0):
    task = remaining.popleft()
    if task == 'noop':
      scheduled.append([1, 0])
    else:
      _, val = task.split(' ')
      scheduled.append([2, int(val)])

  x.append(next_x)

pt1 = 0
for i in [20, 60, 100, 140, 180, 220]:
  pt1 += i*x[i]
print(pt1)

line = ''
for cycle, x_value in enumerate(x):
  pos = cycle % 40
  pixel = '🔥' if x_value - 1 <= pos <= x_value + 1 else '🎄'
  if (pos == 0 and line != ''):
    print(line)
    line = pixel
  else: 
    line += pixel
