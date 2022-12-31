game = { 'win': 6, 'draw': 3, 'lose': 0}
choice = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
# matrix[opponent,me]
matrix = [[3,6,0],[0,3,6],[6,0,3]]
sum=0
with open("input") as file:
    for line in file:
        line = line.strip()
        opponent = choice[line[0]]
        me = choice[line[2]]
        sum += (matrix[opponent-1][me-1]) + me
print(sum)