with open("input") as f:
  instructions = [int(x.strip()) for x in f.readlines()]

pointer = 0
steps = 0
while pointer < len(instructions):
  temp = instructions[pointer]
  instructions[pointer] += 1 #Part 2: if instructions[pointer] < 3 else -1
  pointer += temp
  steps += 1

print(steps)