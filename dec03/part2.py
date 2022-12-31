def priority(a) -> int:
    if ord(a) < 97:
        return ord(a)-38
    else:
        return ord(a)-96

sum = 0
buffer = []
with open("input") as file:
    for line in file:
        buffer.append(line.strip())

for i in range(0,int(len(buffer)/3)):
    first = buffer[i*3]
    second = buffer[i*3+1]
    third = buffer[i*3+2]

    check = {}

    for a in first:
        check[a] = 1
    for a in second:
        if a in check:
            check[a] = 2
    for a in third:
        if a in check and check[a] == 2:
            sum += priority(a)
            break

print(sum)
