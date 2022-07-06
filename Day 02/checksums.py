with open("input") as f:
  lines = [sorted(int(y) for y in x.split()) for x in f.readlines()]

def part1():
  sum = 0
  for line in lines:
    sum += line[-1] - line[0]
  print(sum)

def part2():
  sum = 0
  for line in lines:
    i = len(line) - 1
    while i > 0:
      j = i-1
      while j > -1:
        if line[i] % line[j] == 0:
          sum += int(line[i] / line[j])
          i, j = 0, 0
        j -= 1
      i -= 1
  print(sum)

part1()
part2()