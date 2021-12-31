with open("input.txt") as datafile:
    nav = [[line[0],line[1:].strip()] for line in datafile.readlines()]

for i in nav:
    i[1] = int(i[1])

waypoint = [10,1]
shiploc = [0,0]

for d in nav:
    if d[0] == "N":
        waypoint[1] += d[1]
    if d[0] == "E":
        waypoint[0] += d[1]
    if d[0] == "S":
        waypoint[1] -= d[1]
    if d[0] == "W":
        waypoint[0] -= d[1]
    if d[0] == "F":
        shiploc[0] += d[1] * waypoint[0]
        shiploc[1] += d[1] * waypoint[1]
    if d[0] == "R" or d[0] == "L":
        rotation = d[1] / 90
        if d[0] == "L":
            rotation = 4 - rotation 
            # 3 lefts make a right, makes it so always rotating clockwise
        if rotation >= 2:
            rotation -= 2
            waypoint[0] *= -1
            waypoint[1] *= -1
        if rotation != 0:
            ytemp = waypoint[1]
            waypoint[1] = -1 * waypoint[0]
            waypoint[0] = ytemp


print(shiploc)
print(abs(shiploc[0])+abs(shiploc[1]))