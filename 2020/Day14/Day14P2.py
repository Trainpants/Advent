with open("input.txt") as datafile:
    lines = [line.strip() for line in datafile.readlines()]

dirs = []
mem = dict()
for i in lines:
    x = i.split(" = ")
    if x[0].startswith("mem"):
        x[0] = x[0].strip("me[]")
        x = [int(j) for j in x]
    dirs.append(x)

for k in dirs:
    if k[0] == "mask":
        mask = k[1]
        c = mask.count("X")
    else:
        binary = "{0:036b}".format(k[0])
        formatstr = ""
        for pos,char in enumerate(mask):
            if char == "X":
                formatstr += "%s"
            elif char == "1":
                formatstr += "1"
            else:
                formatstr += binary[pos]
            
        for n in range(2**mask.count("X")):
            Xs = tuple(list("{0:036b}".format(n)[-1*mask.count("X"):]))
            newmem = formatstr % Xs
            mem[int(newmem,2)] = k[1]

memsum = sum(mem.values())
print(memsum) 




# for i in range(1:n+1):
#    binary(i)
#    make a list of individual characters
#    make a list of that list
#    %s those charcters into memory string
#    assign them to the dictionary
