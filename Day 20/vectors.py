def p1():
  with open("input") as f:
    accs = []
    for line in f.readlines():
      l = line.split(",")
      accs.append(sum(abs(i) for i in [int(l[6].split("<")[1]), int(l[7]), int(l[8].split(">")[0])]))
  print(accs.index(0))

def p2():
  #I could check the X equation of each particle and each one could potentially intersect, check the 



  return 0

p1()