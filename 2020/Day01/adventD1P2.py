with open("input.txt") as datafile:
    dataset = [int(i) for i in datafile.readlines()]

underh = []
overh = []

for j in dataset:
    if j < 1010:
        underh.append(j)
    else:
        overh.append(j)

for indx, obj in enumerate(underh):
    m = indx
    o = obj
    for k in range(indx+1,len(underh)):
        if obj + underh[k] < 1010:
            if (2020 - obj - underh[k]) in overh:
                print(obj,underh[k],2020-obj-underh[k])
                print(obj*underh[k]*(2020-obj-underh[k]))
                break
        else:   
            if (2020 - obj - underh[k]) in underh:
                print(obj,underh[k],2020-obj-underh[k])
                print(obj*underh[k]*(2020-obj-underh[k]))
                break

