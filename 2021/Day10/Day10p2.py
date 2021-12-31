with open("input.txt") as datafile:
    data = datafile.read()

nav = data.split("\n")

openers = ["(","[","{","<"]
closers = [")","]","}",">"]
points = [1,2,3,4]
scores = list()

for i in nav:
    line = [char for char in i]
    x = 0
    score = 0
    linescore = ""
    while x < len(line):
        if line[x] in closers:
            if closers.index(line[x]) == openers.index(line[x-1]):
                line.pop(x)
                line.pop(x-1)
                x = -1
                linescore = ""
            else:
                x = len(line)
                linescore = ""
        else:
            linescore += closers[openers.index(line[x])]
        x += 1    

    for i in range(len(linescore),0,-1):
        score = score*5 + closers.index(linescore[i-1])+1
    if score != 0:
        scores.append(score)

sortedscores = sorted(scores)
print(sortedscores[int(len(sortedscores)/2)])