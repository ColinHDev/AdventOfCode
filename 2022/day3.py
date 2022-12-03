def get_character_priority(char: str):
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


priorities: int = 0
for line in open("input.txt", "r"):
    for character in line[:len(line) // 2]:
        if line[len(line) // 2:].count(character) >= 1:
            priorities += get_character_priority(character)
            break

print(str(priorities))
