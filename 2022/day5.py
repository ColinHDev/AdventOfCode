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


def move_crate(amount, fromindex, toindex):
    popIndex = len(crates[fromindex]) - amount
    while amount > 0:
        crates[toindex].append(crates[fromindex][len(crates[fromindex]) - amount])
        crates[fromindex].pop(popIndex)
        amount -= 1


for line in open("input.txt", "r"):
    if not line.startswith("move "):
        continue
    lineParts = line.split(" ")
    move_crate(int(lineParts[1]), int(lineParts[3]) - 1, int(lineParts[5]) - 1)

for stack in crates:
    print(stack[-1], end="")
