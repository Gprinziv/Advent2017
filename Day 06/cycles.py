def cycleRegisters():
  max, addr = 0, 0
  for i in range(len(registers)):
    if registers[i] > max:
      max = registers[i]
      addr = i

  registers[addr] = 0
  
  while max > 0:
    addr = (addr + 1) % len(registers)
    registers[addr] += 1
    max -= 1

def part1():
  steps = 0
  seen = []
  while True:
    cycleRegisters()  

    #Save to a map of previous configurations.
    cyc = registers.copy()
    steps += 1
    if cyc in seen:
      break
    else:
      seen.append(cyc)
  print(steps)
  return cyc

def part2(s):
  cycleRegisters()
  steps = 1
  while registers != s:
    cycleRegisters()
    steps += 1
  print(steps)

with open("input") as f:
  registers = [int(x) for x in f.read().split()]
cyc = part1()
part2(cyc)