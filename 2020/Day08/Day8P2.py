with open("input.txt") as datafile:
    commandlist = [line.strip().split() for line in datafile.readlines()]

for line in commandlist:
    line[1] = int(line[1])

exteriorcount = 1 # count of jmp/nop command that should be switched
boots = False

while boots == False:
    interiorcount = 1 # count of jmp/nop commands encountered in boot run
    ac = 0 # accumulator count
    indx = 0 # current index in boot code
    run_indx = set() # set of already run indices in boot code

    while indx not in run_indx:
        run_indx.add(indx)

        if indx == len(commandlist):
            boots = True
            break
        #elif indx > len(commandlist):
        #    break

        if commandlist[indx][0] == "acc":
            ac += commandlist[indx][1]
            indx += 1

        elif commandlist[indx][0] == "jmp":
            if interiorcount == exteriorcount:
                indx += 1
            else:
                indx += commandlist[indx][1]

        elif commandlist[indx][0] == "nop":
            if interiorcount == exteriorcount:
                indx += commandlist[indx][1]
            else:    
                indx += 1
        interiorcount += 1
        

    exteriorcount += 1

print(ac)