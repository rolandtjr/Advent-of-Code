#!/usr/bin/env python3

def parse_stacks(stacks, line):
    for box in range(9):
        contents = line[box*4+1]
        if contents != ' ':
            match box:
                case 0:
                    stacks[0].append(contents)
                case 1:
                    stacks[1].append(contents)
                case 2:
                    stacks[2].append(contents)
                case 3:
                    stacks[3].append(contents)
                case 4:
                    stacks[4].append(contents)
                case 5:
                    stacks[5].append(contents)
                case 6:
                    stacks[6].append(contents)
                case 7:
                    stacks[7].append(contents)
                case 8:
                    stacks[8].append(contents)


def parse_line(line):
    line = line.strip().split()
    count = int(line[1])
    from_stack = int(line[3]) - 1
    to_stack = int(line[5]) - 1
    return count, from_stack, to_stack


def move_single(stacks, line):
    count, from_stack, to_stack = parse_line(line)

    for _ in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())


def move_multiple(stacks, line):
    count, from_stack, to_stack = parse_line(line)
    count = int(count)

    temp_stack = stacks[from_stack][-count:]
    for _ in range(count):
        stacks[from_stack].pop()
    stacks[to_stack].extend(temp_stack)


def create_and_parse_stacks():
    stacks = [[] for _ in range(9)]

    with open('day5', 'r') as file:
        lines = file.readlines()

    for line in lines[7::-1]:
        parse_stacks(stacks, line[:-1])

    return stacks, lines[10:]


def print_stacks(stacks):
    for stack in stacks:
        print(stack[-1], end='')
    print()


def main():
    stacks, lines = create_and_parse_stacks()

    for line in lines:
        move_single(stacks, line)

    print_stacks(stacks)

    stacks, lines = create_and_parse_stacks()

    for line in lines:
        move_multiple(stacks, line)

    print_stacks(stacks)


if __name__ == '__main__':
    main()
