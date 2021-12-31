# Day 21 Part 1

# Puzzle input:
p1 = 6
p2 = 2

score1 = 0
score2 = 0

turn1 = True
die = 1
rolls = 0

while score1 < 1000 and score2 < 1000:
    roll = 0
    for d in range(3):
        if die > 100:
            die = 1
        roll += die
        die += 1
    if turn1:
        p1 = (p1 + roll) % 10
        if p1 == 0:
            score1 += 10
        else:
            score1 += p1

    else:
        p2 = (p2 + roll) % 10
        if p2 == 0:
            score2 += 10
        else:
            score2 += p2
        
    rolls += 3
    turn1 = not turn1

print(min(score1,score2) * rolls)