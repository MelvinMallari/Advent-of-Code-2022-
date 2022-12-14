from ast import literal_eval
from functools import cmp_to_key

with open('13.txt') as f:
  packets = list(map(literal_eval, [l for l in f if l.strip()]))

def compare(l, r):
  match l, r:
    case int(), int(): 
      return l - r
    case list(), list():
      for f, s in zip(l, r):
        diff = compare(f, s)
        if diff != 0: return diff
      return len(l) - len(r)
    case int(), list():
      return compare([l], r)
    case list(), int():
      return compare(l, [r])

def pt_1():
  res = 0
  for i, (l, r) in enumerate(zip(packets[::2], packets[1::2]), 1):
    if compare(l, r) < 0: res += i
  return res

def divider_index(packets, target):
  return len([p for p in packets if compare(p, target) <= 0])

def pt_2():
  d1, d2 = [[2]], [[6]]
  p = packets + [d1, d2]
  s = sorted(p, key=cmp_to_key(compare))
  return divider_index(s, d1) * divider_index(s, d2)

print(pt_2())