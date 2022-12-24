import re

costs = [map(int, re.findall( "-?\d+", l )) for l in open('19.txt')]
# the possible geodes collected left as a function of time is a triangular number sequence
# https://en.wikipedia.org/wiki/Triangular_number
potential_geodes = [( t - 1 ) * t // 2 for t in range( 32 + 1 )]

res = 0
for bp_id, orbot_ore, cbot_ore, obot_ore, obot_clay, gbot_ore, gbot_obs in costs:
  quality = 0
  max_ore, max_clay, max_obs = max(orbot_ore, cbot_ore, obot_ore, gbot_ore), obot_clay, gbot_obs
  def dfs(t, target_bot, orbots, cbots, obots, gbots, ore, clay, obs, geodes):
    global quality
    if (
      target_bot == 0 and orbots >= max_ore or
      target_bot == 1 and cbots >= max_clay or
      target_bot == 2 and (obots >= max_obs or cbots == 0) or
      target_bot == 3 and obots == 0 or
      geodes + gbots * t + potential_geodes[t] <= quality
    ): return
    # need while loop to keep gathering resources until we can branch & continue dfs (ie make a robot)
    while t:
      if target_bot == 0 and ore >= orbot_ore: # create ore bot
        for b in range(4):
          dfs(t-1, b, orbots+1, cbots, obots, gbots, ore - orbot_ore + orbots, clay + cbots, obs + obots, geodes + gbots)
        return
      elif target_bot == 1 and ore >= cbot_ore: # create clay bot
        for b in range(4):
          dfs(t-1, b, orbots, cbots+1, obots, gbots, ore - cbot_ore + orbots, clay + cbots, obs + obots, geodes + gbots)
        return
      elif target_bot == 2 and ore >= obot_ore and clay >= obot_clay: # create obsidian bot
        for b in range(4):
          dfs(t-1, b, orbots, cbots, obots+1, gbots, ore - obot_ore + orbots, clay - obot_clay + cbots, obs + obots, geodes + gbots)
        return
      elif target_bot == 3 and ore >= gbot_ore and obs >= gbot_obs: # create geodes bot
        for b in range(4):
          dfs(t-1, b, orbots, cbots, obots, gbots+1, ore - gbot_ore + orbots, clay + cbots, obs - gbot_obs + obots, geodes + gbots)
        return
      # if can't create a robot, gather resources
      t, ore, clay, obs, geodes = t - 1, ore + orbots, clay + cbots, obs + obots, geodes + gbots
    quality = max(quality, geodes)
  for bot in range(4):
    dfs(24, bot, 1, 0, 0, 0, 0, 0, 0, 0)
  res += bp_id * quality
print(res)