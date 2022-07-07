with open("input") as f:
  phrases = []
  for line in f.readlines():
    phrases.append([x for x in line.strip().split()])

def isValid(phrase):
  temp = {}
  for word in phrase:
    anagram = sorted(word)
    if word in temp or anagram in temp.values():
      return False
    else:
      temp[word] = anagram
  return True

sum = 0
for phrase in phrases:
  if isValid(phrase):
    sum += 1
print(sum)