from math import floor

#s[0]:(-)N -(+)S
#s[1]:(-)NE-(+)SW
#s[2]:(-)SE-(+)NW
def getSteps(steps):
  # 
  if (steps[1] < 0) ^ (steps[2] > 0):
    ew = abs(steps[1] + steps[2])
    ns = (steps[2] - steps[1]) * (1 if steps[1] > 0 else -1)
    if (steps[0] < 0) ^ (ns < 0):
      if abs(steps[0]) < abs(ns):
        total = ew
      else:
        total = abs(steps[0])
    else:
      total = ew + steps[0]
    return total

  else:
    return steps[0] + max(abs(s) for s in steps[1:]) - abs(steps[1] + steps[2])

def part1(inputs):
  steps = [0, 0, 0]
  directions = {"se": [2, -1], "ne": [1, -1], "n": [0, -1], "nw": [2, 1], "sw": [1, 1], "s": [0, 1]}
  for input in inputs:
    addr, val = directions[input]
    steps[addr] += val

  print(getSteps(steps))    

def part2(inputs):
  steps = [0, 0, 0]
  directions = {"se": [2, -1], "ne": [1, -1], "n": [0, -1], "nw": [2, 1], "sw": [1, 1], "s": [0, 1]}
  max = 0

  for input in inputs:
    addr, val = directions[input]
    steps[addr] += val
    numSteps = getSteps(steps)
    if numSteps > max:
      max = numSteps

  print(max)

with open("input") as f:
  inputs = f.read().split(",")

#part1(inputs)
part2(inputs)