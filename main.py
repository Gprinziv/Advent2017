with open("test") as f:
  inputs = [int(i) for i in f.readline()]
print(inputs)


def test():
  skip, ptr = 0, 0
  rope = [i for i in range(5)]
  print(rope)
  for input in inputs:
    if input + ptr >= len(rope):
      pass
    else:
      rope = rope[:ptr] + rope[ptr:ptr+len:-1] + rope[ptr+len-1]
    print(rope)
    ptr += input + skip
    skip += 1
    print(ptr)
    print(skip)


test()