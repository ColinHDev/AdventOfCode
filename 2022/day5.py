crates = [
    ["T", "P", "Z", "C", "S", "L", "Q", "N"],
    ["L", "P", "T", "V", "H", "C", "G"],
    ["D", "C", "Z", "F"],
    ["G", "W", "T", "D", "L", "M", "V", "C"],
    ["P", "W", "C"],
    ["P", "F", "J", "D", "C", "T", "S", "Z"],
    ["V", "W", "G", "B", "D"],
    ["N", "J", "S", "Q", "H", "W"],
    ["R", "C", "Q", "F", "S", "L", "V"]
]


def move_crate(fromindex, toindex):
    crates[toindex].append(crates[fromindex][-1])
    crates[fromindex].pop()


for line in open("input.txt", "r"):
    if not line.startswith("move "):
        continue
    lineParts = line.split(" ")
    for i in range(int(lineParts[1])):
        move_crate(int(lineParts[3]) - 1, int(lineParts[5]) - 1)

for stack in crates:
    print(stack[-1], end="")
