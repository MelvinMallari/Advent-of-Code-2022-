data = [(l.split()) for l in open('9.txt') ]

dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
move = lambda p, dp: (p[0] + dp[0], p[1] + dp[1])

def solve(length = 1):
  rope =  [(0,0)] * length
  visited = set(rope)

  for d, steps in data:
    for _ in range(int(steps)):
      rope[0] = move(rope[0], dirs[d])
      for i in range(1, len(rope)):
        leader, follower = rope[i-1], rope[i]
        delta = (leader[0] - follower[0], leader[1] - follower[1])
        if abs(delta[0]) > 1 or abs(delta[1]) > 1:
          dx, dy = delta[0] / (abs(delta[0]) or 1),  delta[1] / (abs(delta[1]) or 1)
          rope[i] = move(follower, (dx, dy))
      visited.add(rope[-1])

  return len(visited)


print('pt1', solve(2))
print('pt2', solve(10))