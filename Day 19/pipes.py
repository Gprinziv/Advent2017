def traverse():
  with open("input") as f:
    raw = [x.strip("\n") for x in f.readlines()]

  cur = [0, raw[0].index("|")]
  direction = (1, 0)
  phrase = ""
  count = 0

  while True:
    count += 1
    cur = [sum (i) for i in zip(cur, direction)]
    symbol = raw[cur[0]][cur[1]]
    if symbol == " ":
      print(count)
      return phrase
    if symbol == "+":
      if direction[0] != 0:
        directions = [(0, 1), (0, -1)]
      else:
        directions = [(1, 0), (-1, 0)]

      for newD in directions:
        next = [sum(i) for i in zip(cur, newD)]
        nextSym = raw[next[0]][next[1]]
        if nextSym != " ":
          direction = newD
          break

    elif symbol.isalpha():
      phrase += symbol

final = traverse()
print(final)