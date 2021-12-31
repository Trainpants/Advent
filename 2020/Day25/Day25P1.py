# Day25
def transform(value,subnum):
    return (value*subnum) % 20201227
    

Cardkey = 15733400
Doorkey = 6408062

value = 1
loops = 0
while value != Cardkey:
    value = transform(value,7)
    loops += 1

cardloops = loops
# 3903333

value = 1
loops = 0
while value != Doorkey:
    value = transform(value,7)
    loops += 1

doorloops = loops
# 10459425

value = 1
for i in range(cardloops):
    value = transform(value,Doorkey)

print(value)

value = 1
for j in range(doorloops):
    value = transform(value,Cardkey)

print(value)


