import numpy as np

matrix2d = []
with open("input") as file:
    for line in file:
        matrix2d.append(np.array([int(i) for i in list(line.strip())]))
np2d = np.array(matrix2d)

x,y = np2d.shape
sum = 4*x - 4 # all the edge trees are visible
for i in range(1,x-1):
    for j in range(1,y-1):
        # 4 lines of sight
        left = np.all(np2d[i,j] > np2d[i,0:j])
        right = np.all(np2d[i,j] > np2d[i,j+1:y])
        top = np.all(np2d[i,j] > np2d[0:i,j])
        bottom = np.all(np2d[i,j] > np2d[i+1:x,j])
        if np.any(np.array([left,right,top,bottom])):
            sum += 1
print(sum)
