TEST, INPUT = 3, 363

def part1():
  lock, index = [0], 0
  step = INPUT
  for toInsert in range(1, 2018):
    index = (index + step) % len(lock)
    lock = lock[:index+1] + [toInsert] + lock[index+1:]
    index += 1

  print(lock[index+1])

#Saw a comment on reddit stating that you just needed to record the first value, and I was already doing that in an earlier phase, so I cut out all the needless work.
def part2():
  locksize, index = 1, 0
  for val in range(1, 50000001):
    index = ((index + INPUT) % locksize) + 1
    locksize += 1
    if index == 1:
      print(val)

part2()