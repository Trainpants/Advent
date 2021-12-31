nums = [5,2,8,16,18,0,1]

while len(nums) < 2020:
    if nums.count(nums[len(nums)-1]) == 1:
        nums.append(0)
    else:
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == nums[len(nums)-1]:
                nums.append(len(nums)-1-i)
                break

print(nums[-1])
