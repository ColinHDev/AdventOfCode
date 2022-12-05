inclusions = 0
for line in open("input.txt", "r"):
    [input1, input2] = line.split(",")
    pair1 = input1.split("-")
    pair2 = input2.split("-")
    if int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1]):
        inclusions += 1
    elif int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1]):
        inclusions += 1
print(inclusions)
