with open("input") as f:
    num = f.read()

def part1():
    sum = 0
    for i in range(len(num) - 1):
        if num[i+1] == num[i]:
            sum += int(num[i])
    if num[-1] == num[0]:
        sum += int(num[0])
    print(sum)

def part2():
    sum = 0
    l = int(len(num)/2)
    for i in range(l):
        if num[i] == num[i + l]:
            sum += int(num[i]) * 2
    print(sum)

part1()
part2()