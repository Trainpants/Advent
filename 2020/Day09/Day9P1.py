with open("input.txt") as datafile:
    XMAS = [int(line.strip()) for line in datafile.readlines()]

for indx,num in enumerate(XMAS):
    yesno = False
    if indx > 24:
        for i in range(1,25):
            for j in range(i+1,26):
                if XMAS[indx-i]+XMAS[indx-j] == num:
                    yesno = True
    
    if indx > 24 and yesno == False:
        break

print(num)

