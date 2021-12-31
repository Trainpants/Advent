with open("input.txt") as datafile:
    customs = datafile.readlines()

workstr = ""
worklist = []
sum = 0

for i in customs:
    if i != "\n":
        workstr += i.strip()
        worklist.append(i)    
# this collects a group's data together in a single string, and seperately by person in a list

    else:
        for s in set(workstr):
            if all([(s in l) for l in worklist]):
                sum += 1
# once the entire group's data is collected, converts the string to a set to remove dupes
# then checks that each item in set is in every element of the list

        workstr = ""
        worklist = []

for s in set(workstr):
    if all([(s in l) for l in worklist]):
        sum += 1
# the end of the data doesn't have a "\n", thus the else statement above wouldn't run
# need to repeat that block of code. I could probably find a way to get it to run with repeating
# myself by fuck it this is easier.

print(sum)
# print that shit.


