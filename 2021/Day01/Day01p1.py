with open("input.txt") as datafile:
    data = datafile.read()

depth = data.split("\n")
for i,e in enumerate(depth):
    depth[i] = int(e)
inc = 0

for i,e in enumerate(depth):
    if e > depth[i-1]:
        inc += 1

if depth[0] > depth[-1]:
    inc -= 1

print(inc)

