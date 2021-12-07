#Part 1 
q = float("inf")

for i in range(min(k), max(k) + 1):
    t = sum(abs(x - i) for x in k)
    q = min(q, t)

print(q)

#Part 2
k = list(map(int, data.split(",")))

q = float("inf")

g = lambda x: x * (x + 1) // 2

for i in range(min(k), max(k) + 1):
    t = sum(g(abs(x - i)) for x in k)
    q = min(q, t)

print(q)
