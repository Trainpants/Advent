with open("input.txt") as datafile:
    for line in datafile.readlines():
        schedule = line.strip().split(",")

buses = []
for indx,elem in enumerate(schedule):
    if elem != 'x':
        buses.append([int(elem),indx])
buses.sort()
buses.reverse()

t = 100000000000000
delta = 1

while buses != []:
    t += delta
    for i in buses:
        if (t+i[1])%i[0] == 0:
            delta = delta*i[0]
            buses.remove(i)
        else:
            break

print(t)