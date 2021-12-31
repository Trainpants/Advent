with open("input.txt") as datafile:
    data = datafile.read()

diag = data.split("\n")

o2 = []
co2 = []
d = "0"

count = 0
for i in diag:
    if i[0] == "1":
        count += 1
if count >= len(diag)/2:
    d = "1"

for i in diag:
    if i[0] == d:
        o2.append(i)
    else:
        co2.append(i)

ocount = 1

while len(o2) > 1:
    delete = "1"
    ostr = ""
    for j in o2:
        ostr += j[ocount]
    if ostr.count("1") >= len(ostr)/2:
        delete = "0"
    for k in range(len(ostr)-1,-1,-1):
        if ostr[k] == delete:
            o2.pop(k)
    ocount += 1

cocount = 1
while len(co2) > 1:
    delete = "0"
    costr = ""
    for m in co2:
        costr += m[cocount]
    if costr.count("1") >= len(costr)/2:
        delete = "1"
    for n in range(len(costr)-1,-1,-1):
        if costr[n] == delete:
            co2.pop(n)
    cocount += 1

o2 = o2[0]
co2 = co2[0]

o2dec = 0
co2dec = 0

for z in range(0,len(o2)):
    if o2[-z-1] == "1":
        o2dec += 2**z
    if co2[-z-1] == "1":
        co2dec += 2**z

print(o2dec*co2dec)

