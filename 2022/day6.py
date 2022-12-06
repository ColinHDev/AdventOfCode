def is_marker(marker: str):
    for i in range(0, len(marker) - 1):
        if marker.count(marker[i]) > 1:
            return False
    return True


line = open("input.txt", "r").readline()
markerlength = 14
for i in range(markerlength, len(line)):
    if is_marker(line[i - markerlength:i]):
        print(line[i - markerlength:i] + " => " + str(i))
        break
