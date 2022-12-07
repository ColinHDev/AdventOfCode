"""class Directory:
    name: str
    size_of_files: int = 0
    sub_directories: dict = {}

    def __init__(self, name: str):
        self.name = name

    def get_size(self):
        size = self.size_of_files
        for sub_directory in self.sub_directories:
            size += self.sub_directories[sub_directory].get_size()
        return size


hierarchy: Directory = Directory("/")
current_directory: Directory = Directory("/")
current_hierarchy = ""

for line in open("input.txt", "r"):
    if line.startswith("$ cd "):
        directory = line[5:].replace("\n", "")
        if directory == "/":
            current_directory = hierarchy
            current_hierarchy = "/"
        elif directory == "..":
            current_hierarchy = current_hierarchy[: - (len(current_directory.name) + 1)]
            current_directory = hierarchy
            for parent_directory in current_hierarchy.split("\\"):
                if parent_directory == "/":
                    continue
                current_directory = current_directory.sub_directories[parent_directory]
        else:
            current_directory = current_directory.sub_directories[directory]
            current_hierarchy += "\\" + directory
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir "):
        directory = line[4:].replace("\n", "")
        if directory not in current_directory.sub_directories:
            current_directory.sub_directories[directory] = Directory(directory)
    else:
        current_directory.size_of_files += int(line.split(" ")[0])


def recursive_directory_loop(direc: Directory):
    print(direc.name + " => " + str(direc.get_size()))
    for subdirec in direc.sub_directories:
        recursive_directory_loop(direc.sub_directories[subdirec])


recursive_directory_loop(hierarchy)
#print(hierarchy.sub_directories)
"""

directory_file_sizes = {"/": 0}
directory_hierarchy = {}
current_hierarchy = ""

for line in open("input.txt", "r"):
    if line.startswith("$ cd "):
        directory = line[5:].replace("\n", "")
        if directory == "/":
            current_hierarchy = "/"
        elif directory == "..":
            current_hierarchy = current_hierarchy[: - (len(current_hierarchy.split("\\")[-1]) + 1)]
        else:
            current_hierarchy += "\\" + directory
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir "):
        directory = line[4:].replace("\n", "")
        if current_hierarchy not in directory_hierarchy:
            directory_hierarchy[current_hierarchy] = {}
        directory_hierarchy[current_hierarchy][directory] = True
        dir_hierarchy = current_hierarchy + "\\" + directory
        if dir_hierarchy not in directory_file_sizes:
            directory_file_sizes[dir_hierarchy] = 0
    else:
        directory_file_sizes[current_hierarchy] += int(line.split(" ")[0])


def get_directory_size(hierarchy: str):
    size = directory_file_sizes.get(hierarchy, 0)
    for subdir in directory_hierarchy.get(hierarchy, []):
        size += get_directory_size(hierarchy + "\\" + subdir)
    return size


size_sum = 0
for dir_hierarchy in directory_file_sizes:
    directory_size = get_directory_size(dir_hierarchy)
    if directory_size > 100000:
        continue
    size_sum += directory_size

print(size_sum)