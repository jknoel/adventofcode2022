with open("input") as file:
    for line in file:
        slidingBuffer = []
        i = 0
        while i < len(line):
            if len(slidingBuffer) == 4:
                break
            elif line[i] in slidingBuffer:
                j = slidingBuffer.index(line[i])
                slidingBuffer = slidingBuffer[j+1:len(slidingBuffer)]
            slidingBuffer.append(line[i])
            i += 1
        print(i)