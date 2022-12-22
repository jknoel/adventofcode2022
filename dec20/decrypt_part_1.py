inputList = []
with open("input") as file:
    for line in file:
        line = line.strip()
        inputList.append(int(line)*811589153)
length = len(inputList)
annotatedList = []
oneValueZero = False
for i,value in enumerate(inputList):
    if value == 0:
        if not oneValueZero:
            oneValueZero = True
        else:
            raise Exception("More than one value zero, bad premise.")
    annotatedList.append((i,value))
if not oneValueZero:
    raise Exception("Not at least one value zero, bad premise.")
for mixing in range(0,1):
    for indexToShift in range(0,length):
        for currIndex,(origIndex,value) in enumerate(annotatedList):
            if origIndex == indexToShift:
                newIndex = (currIndex+value-1)%(length-1)+1
                del annotatedList[currIndex]
                annotatedList.insert(newIndex,(origIndex,value))
                break
rearrangedList = []
for origIndex,value in annotatedList:
    rearrangedList.append(value)
zeroIndex = rearrangedList.index(0)
sum = 0
for i in [1000, 2000, 3000]:
    sum = sum + rearrangedList[(zeroIndex+i)%length]
print(sum)