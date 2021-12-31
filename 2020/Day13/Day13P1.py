with open("input.txt") as datafile:
    data = [line.strip() for line in datafile.readlines()]

etd = int(data[0])
buses = set(data[1].split(","))
buses.remove("x")

minwait = etd
mybus = 0

for bus in buses:
    if int(bus) - (etd % int(bus)) < minwait:
        minwait = int(bus) - etd % int(bus)
        mybus = int(bus)

print(minwait * mybus)