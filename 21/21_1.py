import re
from collections import deque

data = [l.strip() for l in open('21.txt')]

def parse():
  res = {}
  for d in data:
    monkey, job = d.split(': ')
    nums = re.findall( "-?\d+", job )
    if nums:
      res[monkey] = int(nums[0])
    else:
      m1, op, m2 = job.split(' ')
      res[monkey] = (m1, m2, op)

  return res

def solve1():
  jobs = parse()
  q = deque()

  for d in data:
    monkey, job = d.split(': ')
    ops = job.split(' ')
    if len(ops) > 1:
      m1, op, m2 = ops
      q.append((monkey, m1, m2, op))

  while q:
    monkey, m1, m2, op = q.pop()
    if isinstance(jobs[m1], int) and isinstance(jobs[m2], int):
      if op == '+':
        jobs[monkey] = int(jobs[m1] + jobs[m2])
      elif op == '-':
        jobs[monkey] = int(jobs[m1] - jobs[m2])
      elif op == '*':
        jobs[monkey] = int(jobs[m1] * jobs[m2])
      elif op == '/':
        jobs[monkey] = int(jobs[m1] / jobs[m2])
    else:
      q.appendleft((monkey, m1, m2, op))
  print(jobs['root'])

def solve2():
  monkeys = {}
  for d in data:
    name, job = d.split(': ')
    if job.isdigit():
      monkeys[name] = int(job)
    else:
      l, op, r = job.split(' ')
      if l in monkeys and r in monkeys:
        monkeys[name] = eval(f"{monkeys[l]} {op} {monkeys[r]}")
      else:
        data.append(d)
  print(monkeys['root'])

solve2()