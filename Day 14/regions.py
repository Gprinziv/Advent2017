from lib2to3.pgen2.token import STRING


TEST = "flqrgnkx-"
INPUT = "wenycdww-"
STRING = INPUT

def makeHash(number):
  inputs = [ord(i) for i in (STRING + number)] + [17, 31, 73, 47, 23]

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

def convertRegion(disk, y, x, val):
  queue = [[y, x]]
  while queue:
    cury, curx = queue.pop(0)
    try:
      if disk[cury][curx] == 1:
        disk[cury][curx] = val
        queue += [[cury, curx+1], [cury, curx-1 if curx > 0 else 0], [cury+1, curx], [cury-1 if cury > 0 else 0, curx]]
    except IndexError:
      continue
  return disk

def part2():
  with open("disk") as f:
    disk = [[int(i) for i in line.strip()] for line in f.readlines()]

  count = 0
  for y in range(128):
    for x in range(128):
      if disk[y][x] == 1:
        count += 1
        disk = convertRegion(disk, y, x, count+1)
  
  print(count)
  return disk

#part1()
#makeDisk()
disk = part2()