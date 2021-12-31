with open("input.txt") as datafile:
    ticketdata = datafile.read()

sections = ticketdata.split("\n\n")

rules = sections[0].split("\n")
for i,e in enumerate(rules):
    e = e.replace("-", " or ")
    e = e.strip("abcdefghijklmnopqrstuvwxyz: ")
    rules[i] = [int(x) for x in e.split(" or ")]

myticket = sections[1].split("\n")[1] # not currently relevant
myticket = [int(y) for y in myticket.split(",")]

tickets = sections[2].split("\n")[1:]
for j,f in enumerate(tickets):
    tickets[j] = [int(z) for z in f.split(",")]


invalids = []
for tick in tickets:
    for item in tick:
        check = 0
        for rule in rules:
            if item in range(rule[0],rule[1]+1) or item in range(rule[2],rule[3]+1):
                check = 1
                break
        if check == 0:
            invalids.append(tick)
            break

for item in invalids:
    tickets.remove(item)

mydic = {}
for i in range(len(rules)):
    for j,rule in enumerate(rules):
        counter = [0]*len(rules)
        for ticket in tickets:
            if ticket[i] in range(rule[0],rule[1]+1) or ticket[i] in range(rule[2],rule[3]+1):
                counter[j] += 1
    
        mydic[counter.index(len(tickets))] = myticket[i]
print(mydic)








