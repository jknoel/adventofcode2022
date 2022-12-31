def priority(a) -> int:
    if ord(a) < 97:
        return ord(a)-38
    else:
        return ord(a)-96

sum = 0
with open("input") as file:
    for line in file:
        line = line.strip()
        first = line[0:int(len(line)/2)]
        second = line[int(len(line)/2):len(line)+1]
        
        if len(first) != len(second):
            raise Exception(f"odd number of characters! {line}")
        
        check = {}

        for a in first:
            check[a] = 1
        for a in second:
            if a in check:
                sum += priority(a)
                break

print(sum)
