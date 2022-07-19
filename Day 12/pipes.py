with open("input") as f:
  pipes = []
  for line in f.readlines():
    routes = line.strip().split(" <-> ")[1]
    pipe = [int(x) for x in routes.split(",")]
    pipes.append(pipe)

def part1():
  seen = {0}
  queue = [0]
  while queue:
    ptr = queue.pop(0)
    for pipe in pipes[ptr]:
      if pipe not in seen:
        seen.add(pipe)
        queue.append(pipe)
  print("PART 1:")
  print(f"Contents of group 0: {seen}")
  print(f"Size of group 0: {len(seen)}")
  print()

def part2():
  seen = []
  queue = []
  unseen = [x for x in range(len(pipes))]
  groups = 0
  while unseen:
    queue.append(unseen[0])
    groups += 1
    while queue:
      ptr = queue.pop(0)
      for pipe in pipes[ptr]:
        if pipe not in seen:
          unseen.remove(pipe)
          seen.append(pipe)
          queue.append(pipe)
  print("PART 2:")
  print(f"Number of groups: {groups}")

part1()
part2()