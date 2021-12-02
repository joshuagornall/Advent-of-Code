instructions = [instruction.split(" ") for instruction in open("input.txt").read().strip().split("\n")]
h, dep, depTwo, aim = 0, 0, 0, 0
for direction, value in instructions:
    value = int(value)
    if direction[0] == "f":
        h += value
        depTwo += value * aim
    elif direction[0] == "d":
        aim += value
        dep += value
    else:
        aim -= value
        dep -= value
print(h * dep) # Answer 1
print(h * depTwo) # Answer 2
