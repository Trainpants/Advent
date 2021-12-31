# Puzzle input:
p1start = 6
p2start = 2

# d3 = 1, 2, 3
# 3d3 - 3x1, 4x3, 5x6, 6x7, 7x6, 8x3, 9x1
# 7 total values, 27 possible rolls

#perms = [(0,0),(1,0),(2,0),(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]
rolls = ["3","4","5","6","7","8","9"]
perms = [0,0,0,1,3,6,7,6,3,1] # leading zeros so index = roll

# what if we measure the turns it takes to get 21 and compare
# for each number of rolls, take the ones that come out above target num
# and multiply the touple of those permutations by the numbers in "rolls"

wins1 = [0]
wins2 = [0]

p1unis = {}
p2unis = {}

for roll in rolls:
    pos1 = (p1start + int(roll)) % 10
    score1 = pos1 or 10
    p1unis[roll] = (pos1,score1)

    pos2 = (p2start + int(roll)) % 10
    score2 = pos2 or 10
    p2unis[roll] = (pos2,score2)

while wins1[-1:] != [0] or len(wins1) < 3:
    blackjacks = 0
    newp1unis = {}
    for uni in p1unis.items():
        for roll in rolls:
            pos1 = (uni[1][0] + int(roll)) % 10
            score1 = pos1 or 10
            if score1 >= 21:
                c = 1
                for letter in uni[0]+roll:
                    c *= perms[int(letter)]
                blackjacks += c
            else:
                newp1unis[uni[0]+roll] = (pos1,score1)
    wins1.append(blackjacks)
    p1unis = newp1unis

while wins2[-1:] != [0] or len(wins2) < 3:
    blackjacks = 0
    newp2unis = {}
    for uni in p2unis.items():
        for roll in rolls:
            pos2 = (uni[1][0] + int(roll)) % 10
            score2 = pos2 or 10
            if score2 >= 21:
                c = 1
                for letter in uni[0]+roll:
                    c *= perms[int(letter)]
                blackjacks += c
            else:
                newp2unis[uni[0]+roll] = (pos2,score2)
    wins2.append(blackjacks)
    p2unis = newp2unis

total1wins = 0

for i,e in enumerate(wins1[2:]):
    minus = 1       
    for j in range(i+2):
        minus = minus * 27 - wins2[j]
    total1wins += minus * e

print(total1wins)
print(wins1)
