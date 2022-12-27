import sympy

ops = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y,
  '/': lambda x, y: x / y,
}

def solve():
  data = [l.strip() for l in open('21.txt')]
  monkeys = { 'humn': sympy.Symbol('x') }
  for d in data:
    name, job = d.split(': ')
    if name in monkeys: continue
    if job.isdigit():
      monkeys[name] = sympy.Integer(job)
    else:
      l, op, r = job.split(' ')
      if l in monkeys and r in monkeys:
        if name == 'root':
          # solve for variable that makes this expression 0
          print(sympy.solve(monkeys[l] - monkeys[r])[0])
          break
        monkeys[name] = ops[op](monkeys[l], monkeys[r])
      else:
        data.append(d)

solve()
