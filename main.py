def test():
  with open("test") as f: instructions = [line for line in f.read().split(",")]
  dancers = list(range(5))

  for inst in instructions:
    if inst[0] == 's':
      val = int(inst[1:])
      dancers = dancers[-val:] + dancers[:-val]
    elif inst[0] == 'p':
      vals = [ord(i) - 97 for i in inst[1:].split("/")]
      a0 = dancers.index(vals[0])
      a1 = dancers.index(vals[1])
      dancers[a0] = vals[1]
      dancers[a1] = vals[0]
    else:
      adds = [int(i) for i in inst[1:].split("/")]
      temp = dancers[adds[0]]
      dancers[adds[0]] = dancers[adds[1]]
      dancers[adds[1]] = temp
  print([chr(c + 97) for c in dancers])

def part1():
  with open("input") as f: instructions = [line for line in f.read().split(",")]
  dancers = list(range(16))
  
  for inst in instructions:
    if inst[0] == 's':
      val = int(inst[1:])
      dancers = dancers[-val:] + dancers[:-val]
    elif inst[0] == 'p':
      vals = [ord(i) - 97 for i in inst[1:].split("/")]
      a0 = dancers.index(vals[0])
      a1 = dancers.index(vals[1])
      dancers[a0] = vals[1]
      dancers[a1] = vals[0]
    else:
      adds = [int(i) for i in inst[1:].split("/")]
      temp = dancers[adds[0]]
      dancers[adds[0]] = dancers[adds[1]]
      dancers[adds[1]] = temp
  print([chr(c + 97) for c in dancers])

def part2():
  #need to do this 1000000000 times, but specific vlaue swaps would fuck with just taking the end result 1000000000 times.
  #instead find the cycle when it resets, and cut out the middleman.
  with open("input") as f: instructions = [line for line in f.read().split(",")]
  dancers = list(range(16))
  count = 0
  twice = 2
  while True:
    for inst in instructions:
      if inst[0] == 's':
        val = int(inst[1:])
        dancers = dancers[-val:] + dancers[:-val]
      elif inst[0] == 'p':
        vals = [ord(i) - 97 for i in inst[1:].split("/")]
        a0 = dancers.index(vals[0])
        a1 = dancers.index(vals[1])
        dancers[a0] = vals[1]
        dancers[a1] = vals[0]
      else:
        adds = [int(i) for i in inst[1:].split("/")]
        temp = dancers[adds[0]]
        dancers[adds[0]] = dancers[adds[1]]
        dancers[adds[1]] = temp
        
    count += 1
    if dancers == list(range(16)):
      break

  print(f"We cycled after {count} dances.")  
  print(dancers)

test()
part1()
part2()