from collections import deque

def parse(): 
  monkeys = {}
  raw_monkeys = open('11.txt', 'r').read().split('\n\n')
  for i, raw_monkey in enumerate(raw_monkeys):
    lines = raw_monkey.split('\n')
    monkeys[i] = {'INSPECTIONS': 0}
    for j, line in enumerate(lines): 
      if (j == 1):
        l = line.split(': ')
        items = l[1].split(', ')
        monkeys[i]['ITEMS'] = deque(int(x) for x in items)
      if (j == 2): 
        operations = line.split(' ')[-2:]
        monkeys[i]['OP_SIGN'] = operations[0]
        monkeys[i]['OP_VALUE'] = operations[1]
      if (j == 3):
        n = line.split(' ')[-1]
        monkeys[i]['TEST'] = int(n)
      if (j == 4):
        m = line.split(' ')[-1]
        monkeys[i]['TRUE'] = int(m)
      if (j == 5):
        m = line.split(' ')[-1]
        monkeys[i]['FALSE'] = int(m)
      
  return monkeys

def inspect(worry, sign, val):
  value = worry if val == 'old' else int(val)
  if (sign == '*'): return worry * value
  if (sign == '+'): return worry + value

monkeys = parse()
def pt_1(rounds = 1):
  for _ in range(rounds):
    for _, monkey in monkeys.items():
      while (len(monkey['ITEMS']) > 0):
        item = monkey['ITEMS'].popleft()
        new_worry = inspect(item, monkey['OP_SIGN'], monkey['OP_VALUE'])
        monkey['INSPECTIONS'] += 1
        new_worry //= 3
        to = monkey['TRUE'] if new_worry % monkey['TEST'] == 0 else monkey['FALSE']
        monkeys[to]['ITEMS'].append(new_worry)

  inspections = []
  for _, monkey in monkeys.items():
    inspections.append(monkey['INSPECTIONS'])
  sorted_inspections = sorted(inspections, reverse=True)

  return sorted_inspections[0] * sorted_inspections[1]

def pt_2(rounds = 1):
  peak_worry = 1
  for monkey in monkeys.values():
    peak_worry *= monkey['TEST']
  for _ in range(rounds):
    for _, monkey in monkeys.items():
      while (len(monkey['ITEMS']) > 0):
        item = monkey['ITEMS'].popleft()
        new_worry = inspect(item, monkey['OP_SIGN'], monkey['OP_VALUE'])
        monkey['INSPECTIONS'] += 1
        new_worry = new_worry % peak_worry
        to = monkey['TRUE'] if new_worry % monkey['TEST'] == 0 else monkey['FALSE']
        monkeys[to]['ITEMS'].append(new_worry)

  inspections = []
  for _, monkey in monkeys.items():
    inspections.append(monkey['INSPECTIONS'])
  sorted_inspections = sorted(inspections, reverse=True)
  return sorted_inspections[0] * sorted_inspections[1]

print(pt_2(10000))
