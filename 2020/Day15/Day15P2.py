mydic = {5:1,2:2,8:3,16:4,18:5,0:6}
myset = {5,2,8,16,18,0}

count = 7
nextnum = 1

while count < 30000000:
    if nextnum in myset:
        x = nextnum
        nextnum = count - mydic[nextnum]
        mydic[x] = count
    else:
        myset.add(nextnum)
        mydic[nextnum] = count
        nextnum = 0
    count += 1

print(nextnum)









