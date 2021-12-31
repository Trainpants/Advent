with open("input.txt") as datafile:
    data = datafile.read()

directions = data.split("\n")

x = 0
y = 0

for i in directions:
	d = int(i[-1])
	if i[0] == "f":
		x += d
	if i[0] == "u":
		y -= d
	if i[0] == "d":
		y += d

print(x*y)