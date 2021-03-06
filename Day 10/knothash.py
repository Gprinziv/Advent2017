def test():
  with open("Day 10/test") as f:
    inputs = [int(i) for i in f.readline().split(", ")]

  skip, ptr = 0, 0
  rope = [i for i in range(5)]
  for input in inputs:
    if input + ptr >= len(rope):
      wrapPtr = (input+ptr)%len(rope)
      invert = (rope[ptr:] + rope[:wrapPtr])[::-1]
      rope = invert[-wrapPtr:] + rope[wrapPtr:ptr] + invert[:-wrapPtr]
    else:
      rope = rope[:ptr] + rope[ptr:ptr+input][::-1] + rope[ptr+input:]

    ptr = (ptr + input + skip) % len(rope)
    skip += 1
  print(rope[0] * rope[1])

def part1():
  with open("Day 10/input") as f:
    inputs = [int(i) for i in f.readline().split(",")]

  skip, ptr = 0, 0
  rope = [i for i in range(256)]
  for input in inputs:
    if input + ptr >= len(rope):
      wrapPtr = (input+ptr)%len(rope)
      invert = (rope[ptr:] + rope[:wrapPtr])[::-1]
      rope = invert[-wrapPtr:] + rope[wrapPtr:ptr] + invert[:-wrapPtr]
    else:
      rope = rope[:ptr] + rope[ptr:ptr+input][::-1] + rope[ptr+input:]

    ptr = (ptr + input + skip) % len(rope)
    skip += 1
  print(rope[0] * rope[1])

def part2():
  with open("Day 10/input") as f:
    inputs = [ord(i) for i in f.readline()] + [17, 31, 73, 47, 23]

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
    
    fin+= hexOr if len(hexOr) == 2 else "0" + hexOr
  print(fin)

test()
part1()
part2()