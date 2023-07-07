#!/usr/bin/env python3

def main():
    with open('day1', 'r') as file:
        lines = file.readlines()

    line = lines[0]
    total = 0
    first = False
    for index, num in enumerate(line):
        try:
            if line[index] == line[index + 1]:
                if first:
                    total += int(num)
                else:
                    total += int(line[index]) + int(line[index + 1])
                    first = True
        except IndexError:
            if line[index] == line[0]:
                total += int(num)

    print(total)

if __name__ == '__main__':
    main()
