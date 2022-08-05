def part1():
  registers = {}
  instructions = []
  with open("input") as f:
    for line in f.readlines():
      inst = line.strip().split(" ")
      instructions.append(inst)
      if inst[1] not in registers:
        registers[inst[1]] = 0

  idx, lastFreq = 0, 0
  while idx < len(instructions):
    inst = instructions[idx]
    idx += 1
    print(f"Instruction: {inst}")
    try:
      i2 = registers[inst[2]] if inst[2].isalpha() else int(inst[2])
    except IndexError:
      i2 = None
    i1 = registers[inst[1]] if inst[1].isalpha() else int(inst[1])

    match inst[0]:
      case "snd":
        lastFreq = i1
      case "set":
        registers[inst[1]] = i2
      case "add":
        registers[inst[1]] += i2
      case "mul":
        registers[inst[1]] *= i2
      case "mod":
        registers[inst[1]] %= i2
      case "rcv":
        if i1 != '0':
          return lastFreq
      case "jgz":
        if i1 > 0:
          idx += (i2 - 1)

class DuetProgram:
  def __init__(self, pID) -> None:
    self.pID = pID
    self.rcv = 0
    self.snd = []
    self.registers = {'p':pID}
    self.idx = 0
    self.sent = 0

  def receive(self, val):
    self.registers[self.rcv] = val
    self.rcv = 0

  def op(self, inst, v1, v2 = None):
    match inst:
      case "add":
        self.registers[v1] += v2
      case "set":
        self.registers[v1] = v2
      case "mul":
        self.registers[v1] *= v2
      case "mod":
        self.registers[v1] %= v2
      case "rcv":
        self.rcv = v1
      case "snd":
        self.snd.append(v1)
        self.sent += 1
      case "jgz":
        if v1 > 0:
          self.idx += v2

  def receiving(self):
    return self.rcv != 0

  def send(self):
    return self.snd.pop(0)

#Ugh, my brain is not in the goddamn mood for this.
def part2():
  with open("input") as f:
    instructions = [x.strip().split(" ") for x in f.readlines()]
  p0 = DuetProgram(0)
  p1 = DuetProgram(1)

  
  while p0.idx < len(instructions) and p1.idx < len(instructions):
    if p0.receiving:
      p1.run()
      if p1.receiving():
        return
    




firstRcv = part1()
print(firstRcv)



