with open("input.txt") as datafile:
    passport = datafile.readlines()

checklist = [0,0,0,0,0,0,0]
valids = 0
field = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]

for line in passport:
    if line == "\n":
        if checklist == [1,1,1,1,1,1,1]:
            valids += 1
        checklist = [0,0,0,0,0,0,0]
    else:
        for i,elem in enumerate(field):
            if elem in line:
                checklist[i] = 1
        
if checklist == [1,1,1,1,1,1,1]:
    valids += 1
print(valids)