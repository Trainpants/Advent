with open("input.txt") as datafile:
    data = datafile.read()

crabs = [int(i) for i in data.split(",")]

minfuel = max(crabs)*len(crabs)

for i in range(min(crabs),max(crabs)+1):
    fuel = 0
    for j in crabs:
        fuel += abs(j-i)
    if fuel < minfuel:
        minfuel = fuel

print(minfuel)