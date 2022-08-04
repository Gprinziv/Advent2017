def dance(instructions, dancers):
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
  return dancers

def test():
  with open("test") as f: instructions = [line for line in f.read().split(",")]
  dancers = dance(instructions, list(range(5)))
  print([chr(c + 97) for c in dancers])

def part1():
  with open("input") as f: instructions = [line for line in f.read().split(",")]
  dancers = dance(instructions, list(range(16)))
  print([chr(c + 97) for c in dancers])

def part2():
  with open("input") as f: instructions = [line for line in f.read().split(",")]
  dancers = list(range(16))
  count = 0
  while True:
    dancers = dance(instructions, dancers)
    count += 1
    if dancers == list(range(16)):
      break
 
  finalCount = 1000000000 % count
  for _ in range(finalCount):
    dancers = dance(instructions, dancers)

  print([chr(c+97) for c in dancers])

test()
part1()
part2()