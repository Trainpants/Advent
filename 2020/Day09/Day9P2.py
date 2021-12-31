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

target = num
weakness = 0 

for indx,num in enumerate(XMAS):
    summ = num
    count = 1
    while summ <= target:
        if summ == target:
            sumlist = [numb for numb in XMAS[indx:(indx+count)]]
            sumlist.sort()
            weakness = sumlist[0]+sumlist[-1]            
            break
        summ += XMAS[indx+count]
        count += 1
    if weakness != 0:
        break

print(weakness)

