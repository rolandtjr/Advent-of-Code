#!/usr/bin/env python3

def find_signal(line):
    letters = [line[x] for x in range(4)]
    for index, letter in enumerate(line[4:]):
        if len(set(letters)) == 4:
            return(index + 4)
        letters[index % 4] = letter


def find_signal_two(line):
    letters = [line[x] for x in range(14)]
    for index, letter in enumerate(line[14:]):
        if len(set(letters)) == 14:
            return(index + 14)
        letters[index % 14] = letter


def main():
    with open('day6', 'r') as file:
        line = file.readlines()

    line = line[0].strip()

    print(find_signal(line))
    print(find_signal_two(line))


if __name__ == '__main__':
    main()
