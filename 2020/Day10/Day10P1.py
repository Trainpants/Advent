with open("input.txt") as datafile:
    adapters = [int(line.strip()) for line in datafile.readlines()]

adapters = sorted(adapters + [0] + [max(adapters)+3])

diff = [adapters[i+1] - adapters[i] for i in range(0,len(adapters)-1)]

print(diff.count(1)*diff.count(3))
