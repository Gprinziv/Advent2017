with open("input") as f:
  garbo = f.readline().strip()

ptr, score, total, uncan = 0, 0, 0, 0
while ptr < len(garbo):
  if garbo[ptr] == "{":
    score += 1
  elif garbo[ptr] == "<":
    uncan += -1
    while garbo[ptr] != ">":
      if garbo[ptr] == "!":
        ptr += 2
      else:
        uncan += 1
        ptr += 1
  elif garbo[ptr] == "!":
    ptr += 1
  elif garbo[ptr] == "}":
    total += score
    score += -1
  ptr += 1

print(f"Final score: {total}")
print(f"Number of garbage chars: {uncan}")