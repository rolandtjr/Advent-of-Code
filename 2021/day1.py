#!/usr/bin/env python3

def main():
    with open('day1', 'r') as file:
        lines = file.readlines()

    prev = lines[0]
    count = 0
    for line in lines[1:]:
        if int(prev) < int(line.strip()):
            count += 1
        prev = line

    print(count)

    prev = int(lines[0]) + int(lines[1]) + int(lines[2])
    count = 0
    for index in range(len(lines) - 3):
        if prev < int(lines[index+1]) + int(lines[index+2]) + int(lines[index+3]):
            count += 1
        prev = int(lines[index+1]) + int(lines[index+2]) + int(lines[index+3])

    print(count)


if __name__ == '__main__':
    main()
