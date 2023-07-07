#!/usr/bin/env python3

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.directories = []
        self.files = []

    def addFile(self, file):
        self.files.append(file)

    def addDirectory(self, directory):
        self.directories.append(directory)

    def getSize(self):
        self.size = 0
        for file in self.files:
            self.size += int(file.size)
        for directory in self.directories:
            self.size += int(directory.getSize())
        return self.size

    def __str__(self):
        return self.name


class FileSystem:
    def __init__(self):
        self.root = Directory('/', '')
        self.root.parent = self.root
        self.current_directory = self.root
        self.all_directories = []

    def addFile(self, file):
        self.root.files.append(file)

    def addDirectory(self, directory):
        self.root.directories.append(directory)

    def getSize(self):
        return self.root.getSize()


def change_directory(line, fs):
    match line[2]:
        case '..':
            fs.current_directory = fs.current_directory.parent
        case '/':
            fs.current_directory = fs.root
        case _:
            for directory in fs.current_directory.directories:
                if directory.name == line[2]:
                    fs.current_directory = directory
                    return
            new_directory = Directory(line[2], fs.current_directory)
            fs.all_directories.append(new_directory)
            fs.current_directory.addDirectory(new_directory)
            fs.current_directory = new_directory


def process_command(line, fs):
    match line[1]:
        case 'cd':
            change_directory(line, fs)
        case 'ls':
            pass


def process_line(line, fs):
    line = line.split()
    match line[0]:
        case '$':
            process_command(line, fs)
        case 'dir':
            for directory in fs.current_directory.directories:
                if directory.name == line[1]:
                    return
            new_directory = Directory(line[1], fs.current_directory)
            fs.all_directories.append(new_directory)
            fs.current_directory.addDirectory(new_directory)
        case _:
            for file in fs.current_directory.files:
                if file.name == line[1]:
                    file.size == line[0]
                    return
            new_file = File(line[1], line[0])
            fs.current_directory.addFile(new_file)


def main():
    with open('day7', 'r') as file:
        lines = file.readlines()

    fs = FileSystem()
    fs.current_directory = fs

    for line in lines:
        line = line.strip()
        process_line(line, fs)

    root_size = fs.getSize()
    print(f'{fs.root.name} : {root_size}')
    max_size = 30_000_000 - (70_000_000 - root_size)
    smallest = 30_000_000
    total_size = 0
    for directory in fs.all_directories:
        size = directory.getSize()
        if size <= 100_000:
            total_size += directory.getSize()
        if size >= max_size:
            if size < smallest:
                smallest = size
    print(total_size)
    print(smallest)


if __name__ == '__main__':
    main()
