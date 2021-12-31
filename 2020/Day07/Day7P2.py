with open("input.txt") as datafile:
    rules = datafile.readlines()

rulelist = [i.strip(".\n").replace(" ","_").split("_bags_contain_") for i in rules]

for bag in rulelist:
    bag[1] = bag[1].split(",_")
    for i,child in enumerate(bag[1]):
        bag[1][i] = child.removesuffix("_bags").removesuffix("_bag").split("_",1)
        if bag[1][i][0] == "no":
            bag[1][0] = [1,"no_bags"]
        else:
            bag[1][i][0] = int(bag[1][i][0])

coefficients = []
innerbags = []
bagsum = 0

for i in rulelist:
    if i[0] == "shiny_gold":
        for b in i[1]:
            coefficients.append(b[0])
            innerbags.append(b[1])

while innerbags != []:
    for bagcheck in rulelist:
        if innerbags[0] == bagcheck[0]:
            bagsum += coefficients[0]
            if len(bagcheck[1]) > 1:
                for indx,multibag in enumerate(bagcheck[1]):
                    if indx > 0:
                        coefficients.append(multibag[0]*coefficients[0])
                        innerbags.append(multibag[1])
            
            innerbags[0] = bagcheck[1][0][1]

            if innerbags[0] == "no_bags":
                del coefficients[0]
                del innerbags[0]
                break
            coefficients[0] *= bagcheck[1][0][0]            
            break

print(bagsum)
