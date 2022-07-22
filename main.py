TEST = "flqrgnkx-"
INPUT = "wenycdww-"

def makeHash(number):
  inputs = [ord(i) for i in (INPUT + number)] + [17, 31, 73, 47, 23]

  skip, ptr = 0, 0
  rope = [i for i in range(256)]
  ropelen = len(rope)
  for _ in range(64):
    for input in inputs:

      #Credit /u/nstyler for the inversion idea. Fixed an error in my own wrap-around code.
      invert = (rope[ptr:] + rope[:(ptr + input) % ropelen])[::-1]
      for i in range(input):
        newPtr = (ptr+i) % ropelen
        rope[newPtr] = invert[i]

      ptr = (ptr + input + skip) % ropelen
      skip += 1

  fin=""
  for i in range(16):
    exOr = 0
    for r in rope[i*16:(i+1)*16]:
      exOr = exOr ^ r
    hexOr = hex(exOr)[2:]
    
    fin += hexOr if len(hexOr) == 2 else "0" + hexOr
  return fin

def part1():
  used = 0
  for i in range(128):
    used += bin(int(makeHash(str(i)), base=16))[2:].count("1")
  print(used)

def makeDisk():
  disk = []
  for i in range(128):
    hash = bin(int(makeHash(str(i)), base=16))[2:]
    while len(hash) < 128:
      hash = "0" + hash
    disk.append(hash)

  with open("disk", 'w') as f:
    for line in disk[:-1]:
      f.write(line + "\n")
    f.write(disk[-1])

def convertRegion(y, x):
  queue = [[y, x]]
  while queue:
    pass
    #If disk[y][x] == 1:
    #  disk[y][x] = "."
    #  queue.append([y+-1, x+-1])
    # Convert the space to a "." and then add all 4 adjacencies to the queue.

#Go into the array provided by disk file, Use a queue and convert 1s to "."s as you find a new region.
def part2():
  with open("disk") as f:
    disk = [i.strip() for i in f.readlines()]

  count = 0
  for y in range(128):
    for x in range(128):
      if disk[y][x] == '1':
        count += 1
        convertRegion(y, x)

  print(count)


#part1()
#makeDisk()
part2()
