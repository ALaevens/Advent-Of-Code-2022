class Directory:
    def __init__(self, name, parent=None):
        self.size: int = 0
        self.name: str = name
        self.parent: Directory = parent
        
        self.children = {}
    
    def add_file(self, name, size):
        if name not in self.children:
            self.children[name] = size

            self.propagate_size(size)

    def add_directory(self, name):
        if name not in self.children:
            self.children[name] = Directory(name, self)

    def propagate_size(self, size):
        self.size += size

        # print(f"[{self.name}] + {size} = {self.size}")

        if self.name == "/":
            return

        self.parent.propagate_size(size)


    def cd(self, arg):
        if arg == "..":
            return self.parent

        elif arg == "/":
            if self.name == "/":
                return self

            new_dir = self.cd("..")
            while new_dir.name != "/":
                new_dir = new_dir.cd("..")

            return new_dir
        
        elif arg in self.children:
            return self.children[arg]

        else:
            return None

def tree(fs_root: Directory, indent=0):
    working_directory = fs_root

    print(f"{'  '*indent}- {working_directory.name} (dir)")
    for child in working_directory.children:
        if isinstance(working_directory.children[child], Directory):
            tree(working_directory.children[child], indent+1)
        else:
            print(f"{' '*(2*indent+1)} {child} (file, size={working_directory.children[child]})")
