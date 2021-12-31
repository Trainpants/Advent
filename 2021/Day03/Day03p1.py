with open("input.txt") as datafile:
    data = datafile.read()

gamma = ""
epsilon = ""

#this loop finds how many bits in binary numbers l
l = 0
while l < len(data):
    if data[l] == "\n":
        break
    l += 1

#this loop counts how many 1s are in each bit position for all numbers
for i in range(0,l):
    x = i
    count = 0
    while x < len(data):
        if data[x] == "1":
            count += 1
        x += l+1
    if count > len(data)/(l+1)/2: #if the count of 1s is greater than half 
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

#converts binary to decimal
gamdec = 0
epsdec = 0
for i in range(0,l):
    if gamma[-i-1] == "1":
        gamdec += 2**i
    else:
        epsdec += 2**i

print(gamdec*epsdec)



