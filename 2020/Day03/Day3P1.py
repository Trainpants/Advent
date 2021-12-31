with open("input.txt") as datafile:
    slope = datafile.readlines()

trees = 0
x = 0

for y in slope:
    if y[x % (len(y)-1)] == '#':
        trees += 1
    x += 3


print(trees)



