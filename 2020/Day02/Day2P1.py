#Advent day 2 part 1
with open("input.txt") as datafile:
    passwords = datafile.readlines()

validpass = 0

for i in passwords:
    count = 0
    workpass = i.split()
    amt = workpass[0].split("-")
    param = workpass[1][0]
    for j in workpass[2]:
        if j == param:
            count += 1
    if count >= int(amt[0]) and count <= int(amt[1]):
        validpass += 1
    
print(validpass)


