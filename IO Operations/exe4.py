




file1 = open('file.txt', 'r')
count = 0
l = []
while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    l.append(line)

file1.close()
print(l)