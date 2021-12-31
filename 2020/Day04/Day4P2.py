def validation(field, data):
    if field in fields:
        i = fields.index(field)

        if i < 3:
            if int(data) in ezparams[i]:
                checklist[i] = 1
        
        if i == 3:
            if data in ezparams[3]:
                checklist[3] = 1

        if i == 4:
            if data[-2:] == "cm" and len(data) == 5:
                if int(data[0:3]) in range(150,194):
                    checklist[4] = 1
            elif data[-2:] == "in" and len(data) == 4:
                if int(data[0:2]) in range(59,77):
                    checklist[4] = 1

        if i == 5:
            if len(data) == 7 and data[0] == "#":
                if set(data[1:]).issubset(set("abcdef1234567890")):
                    checklist[5] = 1

        if i == 6:
            if len(data) == 9 and data.isdigit():
                checklist[6] = 1


with open("input.txt") as datafile:
    passports = datafile.readlines()

checklist = [0,0,0,0,0,0,0]
valids = 0

fields = ["byr","iyr","eyr","ecl","hgt","hcl","pid"]

ezparams = [
    range(1920,2003),
    range(2010,2021),
    range(2020,2031),
    ["amb","blu","brn","gry","grn","hzl","oth"]
]

for line in passports:
    if line == "\n":
        if checklist == [1,1,1,1,1,1,1]:
            valids += 1
        checklist = [0,0,0,0,0,0,0]
    else:
        lineitems = line.strip().split()
        for item in lineitems:
            item = item.split(":")
            validation(item[0],item[1])

if checklist == [1,1,1,1,1,1,1]:
    valids += 1
print(valids)



        


