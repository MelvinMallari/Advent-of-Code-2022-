import re

costs = [map(int, re.findall( "-?\d+", l )) for l in open('19.txt')]

res = 0
for bp_id, orbot_ore, cbot_ore, obot_ore, obot_clay, gbot_ore, gbot_obs in costs:
  bp_quality = 0
  max_ore, max_clay, max_obs = max(orbot_ore, cbot_ore, obot_ore, gbot_ore), obot_clay, gbot_obs
  def dfs(time, target_bot, orbots, cbots, obots, gbots, ore, clay, obs, geode):
    global bp_quality
    # todo: prune DFS here
    if (
      target_bot == 0 and orbots >= max_ore or
      target_bot == 1 and cbots >= max_clay or
      target_bot == 2 and ( obots >= max_obs or cbots == 0 ) or
      target_bot == 3 and obots == 0
    ): return
    # need to do a while loop here to keep gathering resources until we can create a create a branch to continue dfs (make a robot)
    while time:
      if target_bot == 0 and ore >= orbot_ore: # create ore bot
        for b in range(4):
          dfs(time-1, b, orbots+1, cbots, obots, gbots, ore - orbot_ore + orbots, clay + cbots, obs + obots, geode + gbots)
        return
      elif target_bot == 1 and ore >= cbot_ore: # create clay bot
        for b in range(4):
          dfs(time-1, b, orbots, cbots+1, obots, gbots, ore - cbot_ore + orbots, clay + cbots, obs + obots, geode + gbots)
        return
      elif target_bot == 2 and ore >= obot_ore and clay >= obot_clay: # create obsidian bot
        for b in range(4):
          dfs(time-1, b, orbots, cbots, obots+1, gbots, ore - obot_ore + orbots, clay - obot_clay + cbots, obs + obots, geode + gbots)
        return
      elif target_bot == 3 and ore >= gbot_ore and obs >= gbot_obs: # create geode bot
        for b in range(4):
          dfs(time-1, b, orbots, cbots, obots, gbots+1, ore - gbot_ore + orbots, clay + cbots, obs - gbot_obs + obots, geode + gbots)
        return
      # if we can'time create a robot, gather resources
      time, ore, clay, obs, geode = time - 1, ore + orbots, clay + cbots, obs + obots, geode + gbots
    bp_quality = max(bp_quality, geode)
  for bot in range(4):
    dfs(24, bot, 1, 0, 0, 0, 0, 0, 0, 0)
  res += bp_id * bp_quality
print(res)