with open("input") as f:
  tows = [x.split() for x in f.readlines()]


def part1():
  names = set(x[0] for x in tows)
  subs = set(y.strip(",") for x in tows for y in x[3:])
  root = list(names-subs)[0]
  return root

def part2(root):
  tower, towerDict, weights = {}, {}, {}

  for tow in tows:
    if len(tow) > 2:
      towerDict[tow[0]] = [int(tow[1][1:-1])] + [x.strip(",") for x in tow[3:]]
      tower[tow[0]] = [int(tow[1][1:-1])] + [x.strip(",") for x in tow[3:]]
    else:
      weights[tow[0]] = int(tow[1][1:-1])

  while towerDict:
    for key, vals in towerDict.copy().items():
      for i in range(len(vals)):
        if type(vals[i]) == str and vals[i] in weights:
          towerDict[key][i] = weights[vals[i]]
      if all([type(x) == int for x in towerDict[key]]):
        weights[key] = sum(towerDict.pop(key))

  #Get the weight difference off the first one.
  rootWeight = [weights[kid] for kid in tower[root][1:]]
  rootSet = list(set(rootWeight))
  if rootWeight.count(rootSet[0]) == 1:
    diff = rootSet[1] - rootSet[0] 
  else:
    diff = rootSet[0] - rootSet[1]

  while True:
    kidWs = [weights[kid] for kid in tower[root][1:]]
    kidSet = list(set(kidWs))

    if len(set(kidWs)) == 1:
      return tower[root][0] + diff
    
    oddIndex = kidWs.index(kidSet[0] if kidWs.count(kidSet[0]) == 1 else kidSet[1])
    root = tower[root][1 + oddIndex]


root = part1()
print(root)
print(part2(root))