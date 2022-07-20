def part1():
  with open("input") as f:
    sentries = {}
    values = {}
    for line in f.readlines():
      depth, width = [int(x) for x in line.strip().split(": ")]
      sentries[depth] = width
      values[width] = 0

  steps = 0
  total = 0
  while steps <= list(sentries)[-1]:
    if steps in sentries:
      if values[sentries[steps]] == 0:
        total += steps * sentries[steps]

    for key, val in values.items():
      values[key] = (val + 1) % (2*key - 2)
    steps += 1

  print(total)

def part2():
  with open("input") as f:
    sentries = {}
    values = {}
    for line in f.readlines():
      depth, width = [int(x) for x in line.strip().split(": ")]
      sentries[depth] = width
      values[width] = 0

  base = 0
  while True:
    seen = False
    for key, val in sentries.items():
      if (base + key) % (2*val-2) == 0:
        seen = True
        break
    if seen == False:
      return base
    base += 1

#part1()
picoseconds = part2()
print(picoseconds)