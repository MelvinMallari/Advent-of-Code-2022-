from copy import copy
import re

nums_pattern = re.compile(r"-?\d+")

class Valve:
  def __init__(self, name, rate, children):
    self.name = name
    self.rate = rate
    self.children = children

def parse():
  valves = {}
  for line in open('16.txt'):
    _, valve, *_ = line.split()
    rate, = map(int, nums_pattern.findall(line))
    children = re.search(r'valves? (.+)$', line).group(1).split(', ')
    valves[valve] = Valve(valve, rate, children)

  return valves

def floyd_warshall(valves):
  dist = {v: {u: float('inf') for u in valves} for v in valves}

  for v in valves:
    dist[v][v] = 0
    for c in valves[v].children:
      dist[v][c] = 1
  
  for k in valves:
    for i in valves:
      for j in valves:
        dist[i][j] = min(dist[i][j],  dist[i][k] + dist[k][j])
  
  return dist

def solve():
  valves = parse()
  distances = floyd_warshall(valves)
  non_zero_valves = [v for v in valves if valves[v].rate > 0]

  def generate_open_options(curr, opened, time):
    for v in non_zero_valves:
      if v not in opened and distances[curr][v] < time:
        opened.append(v)
        yield from generate_open_options(v, opened, time - distances[curr][v])
        opened.pop()

    yield copy(opened)

  def get_order_score(open_order, time):
    start, res = 'AA', 0
    for pos in open_order:
      time -= distances[start][pos] + 1
      res += valves[pos].rate * time
      start = pos
    return res

  def pt1():
    return max(get_order_score(o, 30) for o in generate_open_options('AA', [], 30))
  
  def pt2():
    paths = list(generate_open_options("AA", [], 26))

    best_scores = {}

    for order in paths:
      tup = tuple(sorted(order))
      score = get_order_score(order, 26)
      best_scores[tup] = max(best_scores.get(tup, 0), score)

    pairs = [(k, v) for k, v in best_scores.items()]

    res = 0
    for human in range(len(pairs) - 1):
      for elephant in range(human + 1, len(pairs)):
        human_path, human_score = pairs[human]
        elephant_path, elephant_score = pairs[elephant]
        for valve in human_path:
          if valve in elephant_path: break
        else:
          res = max(res, human_score + elephant_score)

    return res
  
  print('pt1', pt1())
  print('pt2', pt2())

if __name__ == '__main__':
  solve()