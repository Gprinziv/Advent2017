with open("input") as f:
  instructions = [x.split() for x in f.readlines()]

registers = {}
max = 0

for i in instructions:
  val = int(i[2]) if i[1] == 'inc' else -int(i[2])
  statement = f"registers['{i[4]}'] {i[5]} {i[6]}"
  
  if i[4] not in registers:
    registers[i[4]] = 0
  if i[0] not in registers:
    registers[i[0]] = 0
  if eval(statement):
    registers[i[0]] += val
    if registers[i[0]] > max:
      max = registers[i[0]]

def part1():
  p1max = 0
  for key, val in registers.items():
    if val > p1max:
      p1max = val
  print(p1max)

part1()
print(max)