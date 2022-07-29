#I don't understand the "elegant" solutions yet, so here's brute force.
from itertools import islice

def part1():
  #a, b = 65, 8921
  a, b = 634, 301
  count = 0
  for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a&0xffff == b&0xffff:
      count += 1
  print(count)

#Alright, let's generate!
def genA():
  a = 634
  while True:
    a = (a * 16807) % 2147483647
    if a % 4 == 0:
      yield a

def genB():
  b = 301
  while True:
    b = (b * 48271) % 2147483647
    if b % 8 == 0:
      yield b

def part2():
  A, B = genA(), genB()
  count = 0
  for a, b in islice(zip(A, B), 5000000):
    if a&0xffff == b&0xffff:
      count += 1
  print(count)

part2()