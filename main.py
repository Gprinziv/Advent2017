registers = {}
with open("test") as f:
  instructions = [x.strip().split(" ") for x in f.readlines()]

print(instructions)

