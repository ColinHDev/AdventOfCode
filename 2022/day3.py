def get_character_priority(char: str):
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


priorities: int = 0
lines = open("input.txt", "r").readlines()
for i in range(len(lines) // 3):
    line1, line2, line3 = lines[i * 3], lines[i * 3 + 1], lines[i * 3 + 2]
    for character in line1:
        if line2.count(character) >= 1 and line3.count(character) >= 1:
            priorities += get_character_priority(character)
            break

print(str(priorities))
