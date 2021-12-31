with open("input.txt") as datafile:
    template = [x for x in datafile.readline().strip("\n")]
    inserts = datafile.read().strip("\n").replace(" -> ","\n").split("\n")
    
pairs = {inserts[x]:inserts[x+1] for x in range(0,len(inserts)-1,2)}

for c in range(10):
    i = 0
    while i < len(template)-1:
        template.insert(i+1,pairs[template[i]+template[i+1]])
        i += 2

counts = []
for i in set(template):
    counts.append(template.count(i))

print(max(counts)-min(counts))
