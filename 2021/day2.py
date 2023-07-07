#!/usr/bin/env python3

def main():
    with open('day2', 'r') as file:
        lines = file.readlines()

    position = 0
    depth = 0
    position_2 = 0
    depth_2 = 0
    aim = 0
    for line in lines:
        command = line.split()

        match command[0]:
            case 'forward':
                position += int(command[1])
                position_2 += int(command[1])
                depth_2 += aim * int(command[1])
            case 'up':
                depth -= int(command[1])
                aim -= int(command[1])
            case 'down':
                depth += int(command[1])
                aim += int(command[1])

    print(position * depth)
    print(position_2 * depth_2)


if __name__ == '__main__':
    main()
