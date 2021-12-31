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
    else:
        binary = "{0:036b}".format(k[1])
        output = ""
        for pos,char in enumerate(mask):
            if char == "X":
                output += binary[pos]
            else:
                output += char
        mem[k[0]] = int(output,2)

memsum = sum(mem.values())
print(memsum)