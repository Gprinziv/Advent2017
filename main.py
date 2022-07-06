from math import ceil, sqrt

def part1(pos):
  s = ceil(sqrt(pos))
  if s%2 == 0:
    s += 1
  c = ceil(s/2) - 1
  steps = c + abs(((pos-1) % (s-1)) - c)
  print(steps)



def part2():
  print("I used Excel because life is pain.")
  print(369601)

part1(368078)
part2()