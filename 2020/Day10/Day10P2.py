with open("input.txt") as datafile:
    adapters = [int(line.strip()) for line in datafile.readlines()]

adapters = sorted(adapters + [0] + [max(adapters)+3])

diff = [adapters[i+1] - adapters[i] for i in range(0,len(adapters)-1)]

splitdiff = []
last3 = 0

for i,e in enumerate(diff):
    if e == 3:
        splitdiff.append((diff[last3:i]))
        last3 = i+1

ones = [1,1,2,4,7] # cheating
perms = 1

for split in splitdiff:
    perms = perms * ones[len(split)]


print(perms)
