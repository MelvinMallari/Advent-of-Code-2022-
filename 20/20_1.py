data = [int(l) for l in open('20.txt')]

class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

nodes = [Node(x) for x in data]

# circular linked list
for i, n in enumerate(nodes):
  n.prev = nodes[(i-1)%len(nodes)]
  n.next = nodes[(i+1)%len(nodes)]

for n in nodes:
  if n.val == 0:
    save = n 
    continue

  # convert negative steps to moving forward for simplicity
  steps = n.val % (len(nodes)-1)
  to = n
  for _ in range(steps):
    to = to.next

  if n == to: continue

  # remove the moved node
  n.prev.next = n.next
  n.next.prev = n.prev

  # insert node
  to.next.prev = n
  n.next = to.next
  to.next = n
  n.prev = to

res = 0
for i in range(1, 3001):
  save = save.next
  if i % 1000 == 0: res += save.val
print(res)