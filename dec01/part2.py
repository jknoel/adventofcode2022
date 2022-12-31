with open("input") as file:
    counts = [0]
    for line in file:
        line = line.strip()
        if len(line) > 0:
            counts[-1] += (int(line))
        else:
            counts.append(0)
    counts.sort(reverse=True)
    print(sum(counts[0:3]))