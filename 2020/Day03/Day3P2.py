def sledride(dx,dy):
    x = 0
    treecount = 0
    for indx,elem in enumerate(slope):
        if indx % dy == 0:
            if elem[x % (len(elem)-1)] == '#':
                treecount += 1
            x += dx
    trees.append(treecount)


with open("input.txt") as datafile:
    slope = datafile.readlines()

trees = []
xs = [1,3,5,7,1]
ys = [1,1,1,1,2]
total = 1

for i in range(0,len(xs)):
    sledride(xs[i],ys[i])
    total *= trees[i]

print(trees,total)