with open("input.txt") as datafile:
    customs = datafile.readlines()

workstr = ""
sum = 0

for i in customs:
    if i != "\n":
        workstr += i.strip()
    else:
        sum += len(set(workstr))
        workstr = ""

sum += len(set(workstr))
print(sum)







