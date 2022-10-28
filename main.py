with open("test") as f:
  raw = [x.strip("\n") for x in f.readlines()]

for line in raw:
  print(line)

start = raw[0].index("|")
print(start)