import numpy as np

matrix2d = []
with open("input") as file:
    for line in file:
        matrix2d.append(np.array([int(i) for i in list(line.strip())]))
np2d = np.array(matrix2d)

x,y = np2d.shape
vals = np.zeros([x,y])
for i in range(0,x):
    for j in range(0,y):
        left = np.all(np2d[i,j] > np2d[i,0:j])
        vals[i,j] = 1
        tmp = 0
        for k in range(j-1,0,-1):
            if np2d[i,k] < np2d[i,j]:
                tmp += 1
            else:
                break
        vals[i,j] *= tmp + 1
        tmp = 0
        for k in range(j+1,y-1):
            if np2d[i,k] < np2d[i,j]:
                tmp += 1
            else:
                break
        vals[i,j] *= tmp + 1
        tmp = 0
        for k in range(i-1,0,-1):
            if np2d[k,j] < np2d[i,j]:
                tmp += 1
            else:
                break
        vals[i,j] *= tmp + 1
        tmp = 0
        for k in range(i+1,x-1):
            if np2d[k,j] < np2d[i,j]:
                tmp += 1
            else:
                break
        vals[i,j] *= tmp + 1
        
print(np.max(vals))

