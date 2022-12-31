sum = 0
with open("input") as file:
    for line in file:
        line = line.strip()
        line = line.split(',')
        nums = []
        for a in line:
            a = a.split('-')
            for b in a:
                nums.append(int(b))
        if nums[0] >= nums[2] and nums[1]<=nums[3] or nums[2] >= nums[0] and nums[3]<=nums[1]:
            sum += 1
print(sum)