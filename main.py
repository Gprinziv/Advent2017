base = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]

with open("test") as f:
  rules = [l.strip() for l in f.readlines()]

print(rules)

if len(base) % 2 == 0:
  #New Base needs to be expanded by len(base)/2 units
  newBase = [[0] * (len(base) + 1) for i in range(len(base)) + 1]
  for i in len(base) / 2:
  pass


#for each rule, make a series of posible input patterns (4 rotations)
#size 2 rules are interesting. There are only 6 possible rules:
  #4 .
  #4 #
  #3 .
  #3 #
  #2 # adjacent
  #2 # nonadjacent.

#Size 3 is tougher... Will need to make a map for each, maybe.