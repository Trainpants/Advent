#Advent day 2 part 2
with open("input.txt") as datafile:
    passwords = datafile.readlines()

validpass = 0

for i in passwords:
    workpass = i.split()
    locs = [int(k) for k in workpass[0].split("-")]
    xor = 0
    for j in locs:
        if workpass[2][j-1] == workpass[1][0]:
            xor += 1
    if xor == 1:
        validpass += 1
    
    
print(validpass)

