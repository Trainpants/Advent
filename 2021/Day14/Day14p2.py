with open("input.txt") as datafile:
    template = datafile.readline().strip("\n")
    inserts = datafile.read().strip("\n").replace(" -> ","\n").split("\n")
    
pairs = {inserts[x]:(inserts[x][0]+inserts[x+1],inserts[x+1]+inserts[x][1]) for x in range(0,len(inserts)-1,2)}
counts = {inserts[x]:0 for x in range(0,len(inserts)-1,2)}

for i in range(0,len(template)-1):
    counts[template[i]+template[i+1]] += 1


for c in range(40):
    lastcounts = counts.copy()
    for i in counts:
        counts[i] = 0

    for j in lastcounts:
        counts[pairs[j][0]] += lastcounts[j]
        counts[pairs[j][1]] += lastcounts[j]

elements = dict()
for i in set(template):
    elements[i] = 0

for i in elements:
    for j in counts:
        if i == j[0]:
            elements[i] += counts[j]
        if i == j[1]:
            elements[i] += counts[j]

max = 0
min = 999999999999999999
for k in elements:
    elements[k] /= 2
    if elements[k] > max:
        max = elements[k]
    if elements[k] < min:
        min = elements[k]

print(elements)
print(max-min)

