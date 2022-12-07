from directory import Directory, tree

def part1_sum(current_dir: Directory):
    total = 0
    if current_dir.size <= 100000:
        # print(f"(+) {current_dir.size}")
        total += current_dir.size

    for child in current_dir.children:
        if isinstance(current_dir.children[child], Directory):
            inner_total = part1_sum(current_dir.children[child])
            total += inner_total
    
    return total


with open("input.txt") as f:
    root = Directory("/", True)
    working_directory = root

    adding_files = False

    for line in f:
        segments = line.rstrip().split()

        if segments[0] == "$" and segments[1] == "cd":
            adding_files = False

            working_directory = working_directory.cd(segments[2])

        elif segments[0] == "$" and segments[1] == "ls":
            adding_files = True

        elif adding_files and segments[0] == "dir":
            working_directory.add_directory(segments[1])

        else:
            working_directory.add_file(segments[1], int(segments[0]))

    # tree(root)
    print(part1_sum(root))



