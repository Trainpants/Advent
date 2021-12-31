with open("input.txt") as datafile:
    data = datafile.read()

nav = data.split("\n")

openers = ["(","[","{","<"]
closers = [")","]","}",">"]
points = [3,57,1197,25137]
score = 0

for i in nav:
    line = [char for char in i]
    x = 0
    while x < len(line):
        if line[x] in closers:
            if closers.index(line[x]) == openers.index(line[x-1]):
                line.pop(x)
                line.pop(x-1)
                x = 0
            else:
                score += points[closers.index(line[x])]
                x = len(line)
        x += 1    

print(score)