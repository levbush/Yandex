class Directory:
    def __init__(self, name, parent=None):
        self.name: str = name
        self.parent: Directory | None = parent
        self.files: list[File] = []
        self.directories: list[Directory] = []

    def print_contents(self):
        print('Files: ')
        for file in self.files:
            print(f"{file}")
        print('\nDirectories: ')
        for directory in self.directories:
            print(f"{directory.name}")
        print()


class File:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents
    
    def __str__(self):
        return f"{self.name}"


def retrieve_path(directory: Directory):
    if directory.parent is None:
        return '/'
    else:
        return retrieve_path(directory.parent) + directory.name + '/'


def command_handler(command: list[str]):
    global current_dir
    match command[0]:
        case 'create_directory':
            if len(command) != 2:
                raise ValueError('Invalid command')
            current_dir.directories.append(Directory(command[1], current_dir))
            print(f"Created directory {command[1]} in {retrieve_path(current_dir)}")
        case 'create_file':
            if len(command) != 3:
                raise ValueError('Invalid command')
            current_dir.files.append(File(command[1], command[2]))
            print(f"Created file {command[1]} in {retrieve_path(current_dir)}")
        case 'open':
            if len(command) != 2:
                raise ValueError('Invalid command')
            for directory in current_dir.directories:
                if directory.name == command[1]:
                    current_dir = directory
                    print(f"Opened directory {command[1]}")
                    break
            else:
                for file in current_dir.files:
                    if file.name == command[1]:
                        print(f"Contents of {file.name}:")
                        print(file.contents)
                        break
                else:
                    print(f"Directory or file {command[1]} not found")
        case 'print_contents':
            current_dir.print_contents()
        case 'edit_file':
            command_handler(['create_file', *command[1:]])
        case 'move_up':
            if current_dir.parent is None:
                print("Already at root directory")
            else:
                current_dir = current_dir.parent
        case 'exit':
            exit()
        case _:
            raise ValueError('Invalid command')


root = Directory('/')
current_dir = root


while True:
    print('Current path: ' + retrieve_path(current_dir))
    command = input('create_directory <name> | create_file <name> <contents> \
                    | open <name> | move_up | print_contents | edit_file <name> <contents> | exit\n\n').split()
    try:
        command_handler(command)
    except ValueError as e:
        print(e)