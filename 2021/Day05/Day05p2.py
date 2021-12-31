with open("input.txt") as datafile:
    data = datafile.read()

data = data.replace(" -> ",",")
data = data.split("\n")

ocean = []
vents = []

for i in range(0,1000):
    ocean.append("0"*1000)

for line in data:
    line = [int(i) for i in line.split(",")]
    if line[0] == line[2]:
        if line[1] > line[3]:
            line[1],line[3]=line[3],line[1]
        vents.append(line)
    elif line[1] == line[3]:
        if line[0] > line[2]:
            line[0],line[2]=line[2],line[0]
        vents.append(line)
    elif line[3]-line[1] == line[2]-line[0]:
        if line[0] > line[2]:
            line[0],line[1],line[2],line[3] = line[2],line[3],line[0],line[1]
        vents.append(line)
    else:
        if line[0] > line[2]:
            line[0],line[1],line[2],line[3] = line[2],line[3],line[0],line[1]
        vents.append(line)

for i in vents:
    xs = [j for j in range(i[0],i[2]+1)]
    if i[1]<=i[3]:
        ys = [j for j in range(i[1],i[3]+1)]
    else:
        ys = [j for j in range(i[1],i[3]-1,-1)]
    if len(xs) > len(ys):
        ys *= len(xs)
    if len(ys) > len(xs):
        xs *= len(ys)
    for k in range(len(xs)):
        if ocean[ys[k]][xs[k]] == "0":
            ocean[ys[k]] = ocean[ys[k]][:xs[k]] + "1" + ocean[ys[k]][xs[k]+1:]
        else:
            ocean[ys[k]] = ocean[ys[k]][:xs[k]] + "2" + ocean[ys[k]][xs[k]+1:]

intersections = 0
for m in ocean:
    intersections += m.count("2")

print(ocean)
print(intersections)

