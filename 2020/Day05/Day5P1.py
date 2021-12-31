with open("input.txt") as datafile:
    passlist = datafile.readlines()

maxID = 0

for line in passlist:
    row = [0,127] 
    col = [0,7]  
    
    for i,r in enumerate(line[0:7]):
        if r == "F":
            row[1] -= 2**(6-i)
        if r == "B":
            row[0] += 2**(6-i)

    for i,c in enumerate(line[7:]):
        if c == "R":
            col[0] += 2**(2-i)
        if c == "L":
            col[1] -= 2**(2-i)

    seatID = row[0]*8+col[0]
    if seatID > maxID:
        maxID = seatID
    

print(maxID)


