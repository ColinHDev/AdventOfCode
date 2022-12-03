combinations: dict = {
    "X": {"A": "Z", "B": "X", "C": "Y"},  # losing
    "Y": {"A": "X", "B": "Y", "C": "Z"},  # draw
    "Z": {"A": "Y", "B": "Z", "C": "X"}   # win
}
score: int = 0
for input in open("input.txt", "r"):
    score += (ord(input[2]) - ord("X")) * 3  # (X/Y/Z - X) * 3 = 0/1/2 * 3 = 0/3/6
    playerInput: str = combinations[input[2]][input[0]]
    score += ord(playerInput) - ord("X") + 1  # X/Y/Z - X + 1 = 0/1/2 + 1 = 1/2/3
print(str(score))
