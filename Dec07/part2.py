from directory import Directory, tree

def part2_find(current_dir: Directory, space_required, indent=0):
    print(f"{' '*indent}Analyze {current_dir.name} => {current_dir.size}")

    current_min = current_dir.size
    current_min_name = current_dir.name

    for child in current_dir.children:
        if isinstance(current_dir.children[child], Directory):
            child_dir = current_dir.children[child]
            if child_dir.size >= space_required:
                child_min, min_name = part2_find(child_dir, space_required, indent+1)

                if child_min < current_min:
                    current_min = child_min
                    current_min_name = min_name

    return (current_min, current_min_name)

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

    tree(root)
    free_space = 70000000 - root.size
    space_required = 30000000 - free_space
    print(f"TOTAL SIZE: {root.size}\nFREE SPACE: {free_space}\nREQUIRED: {space_required}")
    print(part2_find(root, space_required))



