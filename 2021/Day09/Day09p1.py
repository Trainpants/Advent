import numpy as np
np.set_printoptions(threshold=np.inf,linewidth=250)

with open("input.txt") as datafile:
    data = datafile.read().split("\n")

cave = np.zeros((len(data[0]),len(data)),np.int8)

for i,e in enumerate(data):
    for j,f in enumerate(e):
        cave[j][i] = int(f)


for y,e in enumerate(cave):
    for x,f in enumerate(e):
        comps = [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]
        if x == 0:
            comps.pop(3)
        if y == 100:
            comps.pop(2)
        if x == 100:
            comps.pop(1)
        if y == 0:
            comps.pop(0)
        for i in comps:
            if f 
