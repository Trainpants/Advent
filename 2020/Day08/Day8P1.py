with open("input.txt") as datafile:
    commandlist = [line.strip().split() for line in datafile.readlines()]

for line in commandlist:
    line[1] = int(line[1])

ac = 0
indx = 0
run_indx = set()

while indx not in run_indx:
    run_indx.add(indx)
    if commandlist[indx][0] == "acc":
        ac += commandlist[indx][1]
        indx += 1
    elif commandlist[indx][0] == "jmp":
        indx += commandlist[indx][1]
    elif commandlist[indx][0] == "nop":
        indx += 1

print(ac)

