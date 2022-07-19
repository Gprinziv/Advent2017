from math import floor

#s[0]:(-)N -(+)S
#s[1]:(-)NE-(+)SW
#s[2]:(-)SE-(+)NW
def getSteps(steps):
  if (steps[1] < 0) ^ (steps[2] > 0): #If both negative/positive (same E/W heading)
    if steps[0] > -steps[1] and steps[0] < steps[2]:
      return abs(steps[1] + steps[2])
    elif steps[1] > 0 and steps[0] < 0:
      return -(steps[0] - steps[2])
    elif steps[1] > 0:
      return steps[0] + steps[1]
    elif steps[0] < 0:
      return -(steps[0] + steps[1])
    else:
      return steps[0] - steps[2]
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