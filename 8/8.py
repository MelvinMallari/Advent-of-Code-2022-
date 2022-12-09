data = [[int(ch) for ch in l.strip()] for l in open('8.txt') ]

def get_directional_arrays(x, y):
  left = [data[x][dy] for dy in range(y-1, -1, -1)]
  right = [data[x][dy] for dy in range(y+1, len(data))]
  up = [data[dx][y] for dx in range(x-1, -1, -1)]
  down = [data[dx][y] for dx in range(x+1, len(data))]
  return left, right, up, down

def pt1():
  total = 0
  for x in range(len(data[0])):
    for y in range(len(data)):
      if x == 0 or x == len(data[0]) - 1 or y == 0 or y == len(data) - 1:
        total += 1
        continue

      left, right, up, down = get_directional_arrays(x, y)

      if all(data[x][y] > height for height in left):
        total += 1
      elif all(data[x][y] > height for height in right):
        total += 1
      elif all(data[x][y] > height for height in up):
        total += 1
      elif all(data[x][y] > height for height in down):
        total += 1

  return total

def score(n, arr):
  score = 1
  for val in arr:
    if val >= n: return score
    score += 1
  return score - 1 

def pt2():
  res = 0 
  for x in range(1, len(data[0]) - 1):
    for y in range(1, len(data) - 1):
      left, right, up, down = get_directional_arrays(x, y)
      curr = data[x][y]
      res = max(res, score(curr, left) * score(curr, right) * score(curr, up) * score(curr, down))

  return res

if __name__ == "__main__":
  print(pt1())
  print(pt2())


