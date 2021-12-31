with open("input.txt") as datafile:
    data = datafile.read()

directions = data.split("\n")

x = 0
y = 0
a = 0

for i in directions:
    d = int(i[-1])
    if i[0] == "f":
        x += d
        y += d*a
    if i[0] == "u":
        a -= d
    if i[0] == "d":
        a += d

print(x*y)