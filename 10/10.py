from collections import deque
data = [l.strip() for l in open('10.txt')]


remaining = deque(data)
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

print(len(x))
line = ''
for cycle in range(len(x)):
  pos = cycle % 40
  pixel = '🔥' if x[cycle] - 1 <= pos <= x[cycle] + 1 else '🎄'
  if (cycle > 0 and pos == 0):
    print(line)
    line = pixel
  else: 
    line += pixel



pt1 = 0
for i, n in enumerate(x, 1):
  if i in set([20, 60, 100, 140, 180, 220]):
    pt1 += i*n
  