with open("input.txt") as datafile:
    data = datafile.read()

depth = data.split("\n")
windows = []
inc = 0
for i,e in enumerate(depth):
    depth[i] = int(e)

for i in range(0,len(depth)-2):
    windows.append(depth[i]+depth[i+1]+depth[i+2])

for i,e in enumerate(windows):
    if e > windows[i-1]:
        inc += 1

if windows[0] > windows[-1]:
    inc -= 1

print(inc)