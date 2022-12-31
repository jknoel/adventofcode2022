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
        dict1 = {}
        for i in range(nums[0],nums[1]+1):
            dict1[f"{i}"] = 1
        for i in range(nums[2],nums[3]+1):
            if f"{i}" in dict1:
                sum += 1
                break
print(sum)