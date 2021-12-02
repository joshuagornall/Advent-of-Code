with open("input.txt") as f:
    input = [int(x) for x in f.read().split("\n")[:-1]]
print(len([x for x in range(1, len(input)) if input[x-1] < input[x]])) # Answer 1
print(len([x for x in range(3, len(input)) if sum(input[x-3:x]) < sum(input[x-2:x+1])])) # Answer 2
