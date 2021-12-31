with open("input.txt") as datafile:
    nav = [[line[0],line[1:].strip()] for line in datafile.readlines()]

for i in nav:
    i[1] = int(i[1])

compass = ["N","E","S","W"]
direction = "E"
x = 0
y = 0

for d in nav:
    if d[0] == "R" or d[0] == "L":
        rotation = d[1] / 90 % 4
        if d[0] == "L":
            rotation = 4 - rotation
        direction = compass[int((compass.index(direction)+rotation) % 4)]
    if d[0] == "F":
        d[0] = direction
    if d[0] == "N":
        y += d[1]
    if d[0] == "E":
        x += d[1]
    if d[0] == "S":
        y -= d[1]
    if d[0] == "W":
        x -= d[1]

print(abs(x)+abs(y))


