winCombinations: dict = {"A": "Y", "B": "Z", "C": "X"}
drawCombinations: dict = {"A": "X", "B": "Y", "C": "Z"}

score: int = 0
for input in open("input.txt", "r"):
    if drawCombinations[input[0]] == input[2]:  # draw
        score += 3
    elif winCombinations[input[0]] == input[2]:  # win
        score += 6
    match input[2]:
        case "X":
            score += 1
        case "Y":
            score += 2
        case "Z":
            score += 3

print(str(score))
