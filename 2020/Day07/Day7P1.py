with open("input.txt") as datafile:
    rules = datafile.readlines()

rulelist = [i.strip(".\n").replace(" ","_").split("_bags_contain_") for i in rules]

for elem in rulelist:
    elem[1] = elem[1].split(",_")
    for i,e in enumerate(elem[1]):
        elem[1][i] = e[2:].removesuffix("_bags").removesuffix("_bag")
    if elem[1][i] == "_other":
        elem[1] = []
    elem.append([])
        
# for loop cleans up data, and seperates into a list of nested lists
# list of bag rule takes form:
# ['bag_color',[children],[empty string for parents]]    

for bags in rulelist:
    for parentcheck in rulelist:
        if bags[0] in parentcheck[1]:
            bags[2].append(parentcheck[0])

# for every bag, goes through list of rules and records every other bags
# that list it as a child in the formally empty list for parents
# each list now takes form ['bag_color',[children],[parents]]

goldparents = set()

for line in rulelist:
    if line[0] == "shiny_gold":
        uncheckedp = line[2]
        for i in uncheckedp:
            goldparents.add(i)
        break

# This initializes a list of parents for the shiny gold bag and an empty set

while uncheckedp != []:
    for line in rulelist:
        if line[0] == uncheckedp[0]:
            for i in line[2]:
                if i not in goldparents:
                    uncheckedp.append(i)
                    goldparents.add(i)
            break
    del uncheckedp[0]

# loops through parents of bags starting with shiny gold until all possible
# parents have been checked, and adds 

print(len(goldparents))