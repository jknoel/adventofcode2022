buffer = []
with open("input") as file:
    for line in file:
        #line = line.strip()
        buffer.append(line)
count = 0
num = None
for line in buffer:
    tokens = line.strip().split(' ')
    if tokens[0] == '1':
        num = count
        numBins = int(tokens[-1])
        break
    count += 1

stacks = []
for i in range(0,numBins):
    stacks.append([])

# read in reverse order
for i in range(num-1,-1,-1):
    for j in range(0,numBins):
        if (j*4+1) < len(buffer[i]):
            char = buffer[i][j*4+1]
            if char != ' ':
                #print(char,j)
                stacks[j].append(char)

for i in range(num+2,len(buffer)): # skip newline
    tokens = buffer[i].strip().split(' ')
    tempStack = []
    for j in range(0,int(tokens[1])):
        item = stacks[int(tokens[3])-1].pop()
        tempStack.append(item)
    for j in range(0,int(tokens[1])):
        item = tempStack.pop()
        stacks[int(tokens[5])-1].append(item)

# final sequence of tops
seq = ''
for i in range(0,numBins):
    seq += stacks[i].pop()

print(seq)


