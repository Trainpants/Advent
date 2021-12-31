with open("input.txt") as datafile:
    data = datafile.read()

fish = [data.count("0"),data.count("1"),data.count("2"),data.count("3"),data.count("4"),data.count("5"),data.count("6"),0,0]

for i in range(80):
    birth = fish.pop(0)
    fish[6] += birth
    fish.append(birth)

print(sum(fish))
