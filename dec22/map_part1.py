# n = 3
# e = 0
# s = 1
# w = 2
colChange = [1,0,-1,0]
rowChange = [0,1,0,-1]
chars = ['>','v','<','^']
numDirections = 4
class Vertex:
    def __init__(self, row, col, typ):
        self.neigh = [None, None, None, None]
        self.row = row
        self.col = col
        self.typ = typ # _ = 1, . = 2, # = 3
        self.newChar = 'x'
    
    def toStringLong(self) -> str:
        ret = f"{self.row} {self.col}\nmy neighbors are:"
        for d in range(0,4):
            if self.neigh[d] is not None:
                ret += f"\ndirection {d}: {self.neigh[d].toStringSimple()}"
        return ret
    
    def toString(self) -> str:
        return f"{self.row+1} {self.col+1}"
    
    def setChar(self,direction):
        self.newChar = chars[direction]
    
    def setup(self, matrix, maxr, maxc):
        
        ii = self.row
        jj = self.col
        if self.typ != ' ':
            for d in range(0,4):
                i = ii + rowChange[d]
                j = jj + colChange[d]
                while matrix[i%maxr][j%maxc].typ not in ['.','#']:
                    i += rowChange[d]
                    j += colChange[d]
                if matrix[i%maxr][j%maxc].typ == '#':
                    self.neigh[d] = None
                else:
                    self.neigh[d] = matrix[i%maxr][j%maxc]

    def getNeighbor(self, d): #d direction
        if self.neigh[d] is not None:
            return self.neigh[d]
        else:
            return self

def changeDirection(d, turn) -> int:
    if turn == 'R':
        shift = 1
    elif turn == 'L':
        shift = -1
    else:
        raise Exception("Bad direction turn!")
    return (d+shift)%numDirections

def getScore(whereami, direction):
    return (whereami.row+1) * 1000 + (whereami.col+1) * 4 + direction

inputfile = "input"
with open(inputfile) as file:
    maxLength = 0
    depth=0
    for line in file:
        if len(line) > maxLength:
            maxLength = len(line)
        depth += 1
    depth -= 2
with open(inputfile) as file:
    matrix = []
    for index1,line in enumerate(file):
        line = line.replace('\n','')
        if len(line) > 0:
            if line[0] in [' ','.','#']:
                matrix.append([])
                for index2,c in enumerate(line):
                    matrix[index1].append(Vertex(index1,index2,c))
                while len(matrix[index1]) < maxLength:
                    matrix[index1].append(Vertex(index1,index2,' '))
            else: 
                task = line.strip()

# set up vertices
whereami = None
for row in range(0,depth):
    for col in range(0,maxLength):
        if matrix[row][col].typ == '.' and whereami is None:
            whereami = matrix[row][col]
        matrix[row][col].setup(matrix,depth,maxLength)

direction = 0 # initial direction
# do the task
while True:
    ri = len(task)+1
    li = len(task)+1
    try:
        ri = task.index('R')
    except Exception:
        pass
    try:
        li = task.index('L')
    except Exception:
        pass
    if ri < li:
        newDirection = changeDirection(direction,'R')
        num = int(task[0:ri])
        task = task[ri+1:len(task)]
    elif li < ri:
        newDirection = changeDirection(direction,'L')
        num = int(task[0:li])
        task = task[li+1:len(task)]
    elif li == ri: # no more L,R; last move!
        num = int(task)
    while num > 0:
        whereami = whereami.getNeighbor(direction)
        whereami.setChar(direction)
        num -= 1
    direction = newDirection
    if li == ri:
        break

print(f"I ended up at: {whereami.toString()}\n with the score: {getScore(whereami,direction)}")
