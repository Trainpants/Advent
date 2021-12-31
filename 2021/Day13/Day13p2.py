import numpy as np
np.set_printoptions(threshold=np.inf,linewidth=100)

with open("input.txt") as datafile:
    data = datafile.read().split("\n\n")

dots = data[0].split("\n")
folds = data[1].split("\n")

for i,e in enumerate(dots):
    dots[i] = e.split(",")
    dots[i][0] = int(dots[i][0])
    dots[i][1] = int(dots[i][1])


for i,e in enumerate(folds):
    folds[i] = e.strip("fold along ").split("=")
    folds[i][1] = int(folds[i][1])

for i in folds:
    c = 0
    if i[0] == "y":
        c = 1
    for j,e in enumerate(dots):
        if e[c] == i[1]:
            dots[j] = dots[j-1]
        if e[c] > i[1]:
            dots[j][c] -= 2*(dots[j][c]-i[1])


dedupe = set()
for i in dots:
    dedupe.add(tuple(i))

drawn = np.zeros((6,40),np.int8)

for i in dedupe:
    drawn[i[1]][i[0]] = 1

print(drawn)
