with open("input.txt") as datafile:
    data = datafile.read()

#data = "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2"

data = data.replace(" -> ",",")
data = data.split("\n")
vents = set()
hor = []
ver = []

for line in data:
    line = line.split(",")
    line = [int(i) for i in line]
    if line[0] == line[2]:
        if line[1] > line[3]:
            line[1],line[3]=line[3],line[1]
        ver.append(line)
    if line[1] == line[3]:
        if line[0] > line[2]:
            line[0],line[2]=line[2],line[0]
        hor.append(line)

for i in range(0,len(hor)):
    for j in range(i+1,len(hor)):
        if hor[i][1] == hor[j][1]:
            for k in range(max(hor[i][0],hor[j][0]),min(hor[i][2],hor[j][2])+1):
                tup = (k,hor[i][1])
                vents.add(tup)

for i in range(0,len(ver)):
    for j in range(i+1,len(ver)):
        if ver[i][0] == ver[j][0]:
            for k in range(max(ver[i][1],ver[j][1]),min(ver[i][3],ver[j][3])+1):
                tup = (ver[i][0],k)
                vents.add(tup)

    for j in range(0,len(hor)):
        if ver[i][0] >= hor[j][0] and ver[i][0] <= hor[j][2]:   
            if hor[j][1] >= ver[i][1] and hor[j][1] <= ver[i][3]:
                tup = (ver[i][0],hor[j][1]) 
                vents.add(tup)

print(len(vents))


