def is_packet_marker(marker: str):
    for i in range(0, len(marker) - 1):
        if marker.count(marker[i]) > 1:
            return False
    return True


line = open("input.txt", "r").readline()
for i in range(3, len(line)):
    if is_packet_marker(line[i - 3:i + 1]):
        print(line[i - 3:i + 1] + " => " + str(i + 1))
        break
