def adjseats(x,y,matrix):
    dirs = [[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]
    adjs = 0 # number of occupied seats in cardinal/intercardinal directions
    for i in dirs:
        c = 1
        while matrix[x+i[0]*c][y+i[1]*c] == ".":
            c += 1
        if matrix[x+i[0]*c][y+i[1]*c] == "#":
            adjs += 1
    return adjs


with open("input.txt") as datafile:
    seats = ["-" + line.strip() + "-" for line in datafile.readlines()]

seats = ["-"*len(seats[0])] + seats + ["-"*len(seats[0])]

newseats = ["-"*len(seats[0])]

while newseats != seats:
    for irow,erow in enumerate(seats[1:len(seats)-1]):
        newrow = "-"
        for icol,ecol in enumerate(seats[irow+1][1:len(seats[0])-1]):
            if ecol != ".":
                adjs = adjseats(irow+1,icol+1,seats)
                if ecol == "L":
                    if adjs == 0:
                        newrow += "#"
                    else:
                        newrow += "L"
                else:
                    if adjs >= 5:
                        newrow += "L"
                    else:
                        newrow += "#"
            else:
                newrow += "."
        newrow += "-"
        newseats += [newrow]

    newseats += ["-"*len(seats[0])]

    if newseats != seats:
        seats = newseats
        newseats = ["-"*len(seats[0])]


sum = 0
for line in seats:
    sum += line.count("#")

print(sum)